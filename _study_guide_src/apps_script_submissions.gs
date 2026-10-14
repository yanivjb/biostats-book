// Study guide: receives (1) explain-it answers that students choose to submit
// for feedback, appended to the "submissions" tab, and (2) thumbs up/down
// ratings of questions, appended to the "ratings" tab, and (3) anonymous practice
// activity (one row per finished question), appended to the "activity" tab. Tabs are
// created automatically the first time something arrives. The "rating_summary" and
// "dashboard" tabs summarize them and update themselves.

const COLUMNS = ["timestamp", "name", "student_code", "question_id", "chapter", "concept",
                 "word_count", "self_check", "answer"];
const RATING_COLUMNS = ["timestamp", "student_code", "question_id", "original_id", "version",
                        "chapter", "outcome", "rating", "reason", "comment"];
const ACTIVITY_COLUMNS = ["timestamp", "student_code", "item", "question_id", "original_id", "version",
                          "chapter", "concepts", "outcome", "attempts", "used_hint", "seconds", "words"];

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const d = JSON.parse(e.postData.contents);
    if (d.kind === "activity") {
      const row = ACTIVITY_COLUMNS.map(k => k === "timestamp" ? new Date() : clean_(d[k]));
      getActivityTab_().appendRow(row);
    } else if (d.kind === "rating") {
      const row = RATING_COLUMNS.map(k => k === "timestamp" ? new Date() : clean_(d[k]));
      getRatingsTab_().appendRow(row);
    } else {
      const row = COLUMNS.map(k => k === "timestamp" ? new Date() : clean_(d[k]));
      getTab_().appendRow(row);
    }
    return ContentService.createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

// Visiting the web app URL in a browser shows this, which confirms the deployment works.
function doGet() {
  return ContentService.createTextOutput("Study guide submissions are open.");
}

function getTab_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName("submissions");
  if (!sheet) {
    sheet = ss.insertSheet("submissions");
    sheet.appendRow(COLUMNS);
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function getRatingsTab_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName("ratings");
  if (!sheet) {
    sheet = ss.insertSheet("ratings");
    sheet.appendRow(RATING_COLUMNS);
    sheet.setFrozenRows(1);
    // One row per question: thumbs up, thumbs down, comments; most-disliked first.
    const summary = ss.getSheetByName("rating_summary") || ss.insertSheet("rating_summary");
    summary.getRange("A1").setFormula(
      '=QUERY(ratings!A:J, "select C, E, count(A) where H is not null group by C, E pivot H order by C", 1)');
    summary.getRange("F1").setValue("Questions with the most thumbs down:");
    summary.getRange("F2").setFormula(
      '=IFERROR(QUERY(ratings!A:J, "select C, count(A) where H = \'down\' group by C order by count(A) desc label count(A) \'thumbs down\'", 1), "none yet")');
  }
  return sheet;
}

// Columns: A timestamp, B student_code, C item, D question_id, E original_id, F version,
// G chapter, H concepts, I outcome, J attempts, K used_hint, L seconds, M words.
// Outcomes: first (right on the first try), retry (right after a wrong try or a hint),
// revealed (gave up and looked), skipped, self-yes / self-partly / self-no (self-rated).
function getActivityTab_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName("activity");
  if (!sheet) {
    sheet = ss.insertSheet("activity");
    sheet.appendRow(ACTIVITY_COLUMNS);
    sheet.setFrozenRows(1);
    makeDashboard_(ss);
  }
  return sheet;
}

// Run this from the Apps Script editor to rebuild the dashboard tab if it gets messed up.
function rebuildDashboard() {
  makeDashboard_(SpreadsheetApp.getActiveSpreadsheet());
}

function makeDashboard_(ss) {
  const d = ss.getSheetByName("dashboard") || ss.insertSheet("dashboard");
  d.clear();
  const A = "activity!";
  const checked = A + 'C2:C,"checked"';
  d.getRange("A1").setValue("Overall").setFontWeight("bold");
  d.getRange("A2:B8").setValues([
    ["Questions finished", "=COUNTA(" + A + "A2:A)"],
    ["Students (browsers)", "=COUNTUNIQUE(" + A + "B2:B)"],
    ["Checked questions answered (not skipped)", "=COUNTIFS(" + checked + "," + A + 'I2:I,"<>skipped")'],
    ["% right on the first try", "=IFERROR(COUNTIFS(" + checked + "," + A + 'I2:I,"first")/B4,"")'],
    ["% right after a retry or hint", "=IFERROR(COUNTIFS(" + checked + "," + A + 'I2:I,"retry")/B4,"")'],
    ["% gave up and looked", "=IFERROR(COUNTIFS(" + checked + "," + A + 'I2:I,"revealed")/B4,"")'],
    ["Median seconds per question", '=IFERROR(MEDIAN(FILTER(' + A + 'L2:L,' + A + 'C2:C="checked")),"")']
  ]);
  d.getRange("B5:B7").setNumberFormat("0%");
  d.getRange("A10").setValue("Per day").setFontWeight("bold");
  d.getRange("A11").setFormula('=IFERROR(QUERY(' + A + 'A:M, "select toDate(A), count(A) where A is not null group by toDate(A) order by toDate(A) desc label toDate(A) \'day\', count(A) \'questions finished\'", 1), "none yet")');
  d.getRange("D1").setValue("By chapter (counts of each outcome, checked questions)").setFontWeight("bold");
  d.getRange("D2").setFormula('=IFERROR(QUERY(' + A + 'A:M, "select G, count(A) where C = \'checked\' group by G pivot I", 1), "none yet")');
  d.getRange("D20").setValue("By question (counts of each outcome; sort to find the hardest)").setFontWeight("bold");
  d.getRange("D21").setFormula('=IFERROR(QUERY(' + A + 'A:M, "select E, count(A) where C = \'checked\' group by E pivot I", 1), "none yet")');
  d.setColumnWidth(1, 280);
}

// Keep cells reasonable and stop spreadsheet formulas from being injected.
function clean_(v) {
  if (v === undefined || v === null) return "";
  let s = typeof v === "string" ? v : JSON.stringify(v);
  s = s.slice(0, 5000);
  return /^[=+\-@]/.test(s) ? "'" + s : s;
}
