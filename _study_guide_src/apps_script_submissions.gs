// Study guide: receives (1) explain-it answers that students choose to submit
// for feedback, appended to the "submissions" tab, and (2) thumbs up/down
// ratings of questions, appended to the "ratings" tab. Tabs are created
// automatically the first time something arrives. The "rating_summary" tab
// tallies ratings per question and updates itself.

const COLUMNS = ["timestamp", "name", "student_code", "question_id", "chapter", "concept",
                 "word_count", "self_check", "answer"];
const RATING_COLUMNS = ["timestamp", "student_code", "question_id", "original_id", "version",
                        "chapter", "outcome", "rating", "reason", "comment"];

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const d = JSON.parse(e.postData.contents);
    if (d.kind === "rating") {
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

// Keep cells reasonable and stop spreadsheet formulas from being injected.
function clean_(v) {
  if (v === undefined || v === null) return "";
  let s = typeof v === "string" ? v : JSON.stringify(v);
  s = s.slice(0, 5000);
  return /^[=+\-@]/.test(s) ? "'" + s : s;
}
