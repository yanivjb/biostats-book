import pandas as pd,numpy as np,statsmodels.formula.api as smf,matplotlib,sys
matplotlib.use('Agg'); import matplotlib.pyplot as plt
P='../peng/p.csv'
def gentoo():
    p=pd.read_csv(P); g=p[p.species=='Gentoo'].dropna(subset=['sex','bill_length_mm','bill_depth_mm'])
    m=smf.ols('bill_depth_mm ~ bill_length_mm + sex',g).fit()
    fig,ax=plt.subplots(figsize=(7,5),dpi=150); cols={'female':'#E8746B','male':'#2BB3BF'}
    for s,d in g.groupby('sex'):
        ax.scatter(d.bill_length_mm,d.bill_depth_mm,s=45,alpha=.7,color=cols[s],label=s)
        xs=np.linspace(d.bill_length_mm.min(),d.bill_length_mm.max(),50)
        ax.plot(xs,m.predict(pd.DataFrame({'bill_length_mm':xs,'sex':s})),color=cols[s],lw=3)
        b=np.polyfit(d.bill_length_mm,d.bill_depth_mm,1); ax.plot(xs,np.polyval(b,xs),'--',color=cols[s],lw=2)
    ax.set_xlabel('bill_length_mm',fontsize=14); ax.set_ylabel('bill_depth_mm',fontsize=14)
    ax.set_xticks(range(40,62,2)); ax.set_yticks(np.arange(13,18.5,0.5)); ax.grid(alpha=.4)
    ax.legend(title='sex',loc='upper left',fontsize=12)
    fig.tight_layout(); fig.savefig('bank_images/ch13-book-gentoo-resid.png')
gentoo() if len(sys.argv)>1 and sys.argv[1]=="all" else None

def iris_AB():
    i=pd.read_csv('../peng/iris.csv'); rng=np.random.default_rng(3)
    sp=['setosa','versicolor','virginica']; cols=dict(zip(sp,['#E8746B','#55B04B','#6A9BF4']))
    means=i.groupby('species').sepal_length.mean()
    fig,ax=plt.subplots(figsize=(6.5,5),dpi=150)
    A=i[(i.species=='setosa')&(i.sepal_length==5.7)].index[0]; B=i[(i.species=='virginica')&(i.sepal_length==5.8)].index[0]
    for k,s in enumerate(sp):
        d=i[i.species==s]; x=k+rng.uniform(-.18,.18,len(d))
        ax.scatter(x,d.sepal_length,s=30,alpha=.55,color=cols[s])
        ax.hlines(means[s],k-.3,k+.3,color='black',lw=2.5)
        for lab,idx in (('A',A),('B',B)):
            if idx in d.index:
                xx=x[list(d.index).index(idx)]
                ax.scatter([xx],[i.sepal_length[idx]],s=160,facecolors='none',edgecolors='black',lw=2)
                ax.annotate(lab,(xx,i.sepal_length[idx]),xytext=(14,6),textcoords='offset points',fontsize=16,weight='bold')
    ax.set_xticks(range(3)); ax.set_xticklabels(sp,fontsize=13); ax.set_ylabel('Sepal.Length (cm)',fontsize=14)
    ax.set_yticks(np.arange(4.0,8.1,0.2),minor=True); ax.set_yticks(np.arange(4,8.1,0.5)); ax.grid(axis='y',which='both',alpha=.35)
    ax.set_title('Black lines: species means from lm(Sepal.Length ~ Species)',fontsize=10)
    fig.tight_layout(); fig.savefig('bank_images/ch13-chimein-iris-AB.png')

def fish():
    rng=np.random.default_rng(11); n_e,n_u=13,15
    age=np.r_[rng.uniform(1.5,9,n_e),rng.uniform(1,12,n_u)].round(1)
    ex=np.r_[np.ones(n_e),np.zeros(n_u)]
    mu=1.25+0.45*ex-0.04*age; e=rng.normal(0,1,len(age))
    X=np.c_[np.ones(len(age)),ex,age]; e=e-X@np.linalg.lstsq(X,e,rcond=None)[0]
    e=e*np.sqrt(2.45/np.sum(e**2)); cv=mu+e
    d=pd.DataFrame(dict(cv=cv.round(4),exploited=np.where(ex==1,'yes','no'),age=age))
    d.to_csv('src/fish_simulated.csv',index=False)
    m=smf.ols('cv ~ exploited + age',d).fit()
    fig,ax=plt.subplots(figsize=(6.5,5),dpi=150); cols={'yes':'#D55E00','no':'#0072B2'}; lab={'yes':'exploited','no':'unexploited'}
    for s,g in d.groupby('exploited'): ax.scatter(g.age,g.cv,s=50,alpha=.8,color=cols[s],label=lab[s])
    ax.set_xlabel('Age at maturation (years)',fontsize=14); ax.set_ylabel('CV of larval abundance',fontsize=14)
    ax.set_xlim(0,13); ax.set_xticks(range(0,14)); ax.grid(alpha=.35); ax.legend(fontsize=12)
    fig.tight_layout(); fig.savefig('bank_images/ch13-quiz-fish.png')
    print(m.params.round(3).to_dict(),'RSS',round(m.ssr,3),'MS',round(m.mse_resid,4),'sd',round(np.sqrt(m.mse_resid),3),'df',m.df_resid)
    print(d.groupby('exploited').cv.agg(['mean','count']).round(3)); print(d.age.describe().round(2).to_dict())
if __name__=='__main__':
    iris_AB(); fish()

def normal_funcs():
    from scipy.stats import norm
    xs=np.linspace(-3.5,3.5,400); fig,ax=plt.subplots(figsize=(6.5,4.2),dpi=150)
    ax.plot(xs,norm.pdf(xs),color='black',lw=2); x0=1.0
    ax.fill_between(xs[xs>=x0],norm.pdf(xs[xs>=x0]),color='#6A9BF4',alpha=.5)
    ax.vlines(x0,0,norm.pdf(x0),color='#D55E00',lw=2.5); ax.scatter([x0],[norm.pdf(x0)],color='#D55E00',zorder=3,s=40)
    ax.annotate('y (height of the curve at x)',(x0,norm.pdf(x0)),xytext=(1.4,0.33),fontsize=10,arrowprops=dict(arrowstyle='->'))
    ax.annotate('shaded area: P(value > x)',(1.6,0.05),xytext=(2.0,0.17),fontsize=10,arrowprops=dict(arrowstyle='->'))
    ax.set_xticks([x0]); ax.set_xticklabels(['x'],fontsize=14); ax.set_yticks([]); ax.set_ylim(0,.45)
    ax.set_ylabel('probability density',fontsize=12); ax.spines[['top','right']].set_visible(False)
    fig.tight_layout(); fig.savefig('bank_images/ch14-chimein-norm-functions.png')

def bluetit():
    rng=np.random.default_rng(7); n=3720
    main=rng.normal(11.2,0.85,int(n*0.88)); tail=rng.normal(8.6,1.5,n-int(n*0.88))
    m=np.r_[main,tail]; m=m[(m>3)&(m<14.5)]
    fig,ax=plt.subplots(figsize=(6.5,4.2),dpi=150)
    ax.hist(m,bins=60,color='#7AA6C2',edgecolor='white')
    ax.set_xlabel('Chick mass at 14 days (g)',fontsize=13); ax.set_ylabel('Number of chicks',fontsize=13)
    ax.set_title(f'Blue tit chicks (n = {len(m):,})',fontsize=11); ax.spines[['top','right']].set_visible(False)
    fig.tight_layout(); fig.savefig('bank_images/ch14-hw-bluetit.png')
    print('bluetit n',len(m))
if __name__=='__main__':
    normal_funcs(); bluetit()

def hyena_qq():
    from scipy import stats
    d=np.array([0.123,0.183,-0.017,0.189,0.113,0.164,0.096,-0.097,0.061])
    (osm,osr),(sl,ic,_)=stats.probplot(d,dist='norm')
    fig,ax=plt.subplots(figsize=(5,4.2),dpi=150)
    ax.scatter(osm,osr,s=45,color='#444'); xs=np.array([osm.min()-.2,osm.max()+.2]); ax.plot(xs,ic+sl*xs,color='#D55E00',lw=2)
    ax.set_xlabel('Theoretical quantiles (normal)',fontsize=12); ax.set_ylabel('Giggle difference\n(subordinate - dominant)',fontsize=12)
    ax.grid(alpha=.35); fig.tight_layout(); fig.savefig('bank_images/ch15-book-hyena-qq.png')
if __name__=='__main__':
    hyena_qq()

def _ci(ax,x,v,color='black'):
    from scipy import stats
    m=v.mean(); h=stats.t.ppf(.975,len(v)-1)*v.std(ddof=1)/np.sqrt(len(v))
    ax.errorbar([x],[m],yerr=[h],fmt='o',color=color,capsize=8,lw=2,ms=7,zorder=4)
def frogs():
    import io
    f=pd.read_csv('src/frogs.csv'); f.columns=[c.strip().replace('﻿','') for c in f.columns]
    rng=np.random.default_rng(1); cols={'nonpreferred':'#E8746B','preferred':'#2BB3BF'}
    fig,ax=plt.subplots(figsize=(5.5,4.5),dpi=150)
    for k,t in enumerate(['nonpreferred','preferred']):
        v=f[f.treatment==t]['hatched.eggs']; ax.scatter(k+rng.uniform(-.15,.15,len(v)),v,alpha=.6,color=cols[t],s=35); _ci(ax,k,v)
    ax.set_xticks([0,1]); ax.set_xticklabels(['nonpreferred','preferred'],fontsize=12); ax.set_ylabel('hatched_eggs',fontsize=13); ax.set_xlim(-.6,1.6); ax.grid(axis='y',alpha=.35)
    ax.set_title('Points: individual pairs. Black: mean ± 95% CI',fontsize=10); fig.tight_layout(); fig.savefig('bank_images/ch16-book-frogs.png')
    fig,axs=plt.subplots(1,3,figsize=(10,3.4),dpi=150,sharey=True); bins=np.linspace(0,1000,13)
    axs[0].hist(f['hatched.eggs'],bins=bins,color='#888',edgecolor='white'); axs[0].set_title('(A) both treatments combined',fontsize=10)
    for ax,t in zip(axs[1:],['nonpreferred','preferred']):
        ax.hist(f[f.treatment==t]['hatched.eggs'],bins=bins,color=cols[t],edgecolor='white'); ax.set_title(f'(B) {t}',fontsize=10)
    for ax in axs: ax.set_xlabel('hatched_eggs')
    axs[0].set_ylabel('count'); fig.tight_layout(); fig.savefig('bank_images/ch16-book-frog-hists.png')
def trout():
    import io
    t=pd.read_csv(io.StringIO(open('src/chap12e4ChinookWithBrookTrout.csv',newline='').read().replace('\r','\n')))
    rng=np.random.default_rng(2); fig,ax=plt.subplots(figsize=(5.5,4.5),dpi=150); cols={'absent':'#0072B2','present':'#D55E00'}
    for k,g in enumerate(['absent','present']):
        v=t[t.troutTreatment==g].proportionSurvived; ax.scatter(k+rng.uniform(-.12,.12,len(v)),v,alpha=.7,color=cols[g],s=45); _ci(ax,k+.3,v)
    ax.set_xticks([0,1]); ax.set_xticklabels(['brook trout absent','brook trout present'],fontsize=11); ax.set_ylabel('Proportion of Chinook surviving',fontsize=12)
    ax.set_xlim(-.5,1.7); ax.grid(axis='y',alpha=.35); ax.set_title('Points: streams. Black: mean ± 95% CI',fontsize=10)
    fig.tight_layout(); fig.savefig('bank_images/ch16-hw-trout.png')
if __name__=='__main__':
    frogs(); trout()

def deviations(order, labels, fname):
    h=pd.read_csv('../hz.csv').rename(columns={'cutoff0.9':'admix'})
    d=h[(h.admix.notna())&(h.petal_color.notna())&(h.subsp=='P')&(h.site=='S22')].copy()
    d['gm']=d.admix.mean(); d['yhat']=d.groupby('petal_color').admix.transform('mean')
    d=d.sort_values(['petal_color','admix']).reset_index(drop=True); d['x']=np.arange(len(d))
    cols={'pink':'#D95F9E','white':'#7F7F7F'}
    kinds={'error':('admix','yhat'),'model':('yhat','gm'),'total':('admix','gm')}
    fig,axs=plt.subplots(1,3,figsize=(11,3.6),dpi=150,sharey=True)
    for ax,k,lab in zip(axs,order,labels):
        a,b=kinds[k]
        ax.vlines(d.x,d[a],d[b],color=[cols[c] for c in d.petal_color],lw=1.5)
        ax.scatter(d.x,d.admix,s=18,color=[cols[c] for c in d.petal_color],zorder=3)
        ax.axhline(d.gm.iloc[0],color='black',lw=1.2)
        for c,g in d.groupby('petal_color'): ax.hlines(g.yhat.iloc[0],g.x.min()-.4,g.x.max()+.4,color=cols[c],lw=2.5,linestyle='--')
        ax.set_title(lab,fontsize=14,weight='bold'); ax.set_xticks([])
    axs[0].set_ylabel('admixture proportion',fontsize=12)
    fig.text(.5,.01,'individual plants (pink, then white). Black line: grand mean; dashed: group means',ha='center',fontsize=9)
    fig.tight_layout(rect=(0,.04,1,1)); fig.savefig('bank_images/'+fname)
if __name__=='__main__':
    deviations(['error','total','model'],['A','B','C'],'ch17-book-deviations.png')
    deviations(['total','model','error'],['plot 1','plot 2','plot 3'],'ch17-hw-deviations.png')

def dev_generic(d,y,g,order,labels,fname,ylab,jit=0.0):
    pal=['#E8746B','#55B04B','#6A9BF4','#C77CFF','#D89000','#00A9A5']
    lv=sorted(d[g].unique()); cols=dict(zip(lv,pal))
    d=d.copy(); d['gm']=d[y].mean(); d['yhat']=d.groupby(g)[y].transform('mean')
    d=d.sort_values([g,y]).reset_index(drop=True); d['x']=np.arange(len(d))+d[g].map({l:i*3 for i,l in enumerate(lv)})
    kinds={'error':(y,'yhat'),'model':('yhat','gm'),'total':(y,'gm')}
    fig,axs=plt.subplots(1,3,figsize=(12,3.8),dpi=150,sharey=True)
    for ax,k,lab in zip(axs,order,labels):
        a,b=kinds[k]; c=[cols[v] for v in d[g]]
        ax.vlines(d.x,d[a],d[b],color=c,lw=1.1); ax.scatter(d.x,d[y],s=12,color=c,zorder=3)
        ax.axhline(d.gm.iloc[0],color='black',lw=1.2)
        for v,gg in d.groupby(g): ax.hlines(gg.yhat.iloc[0],gg.x.min()-.5,gg.x.max()+.5,color=cols[v],lw=2.5)
        ax.set_title(lab,fontsize=14,weight='bold'); ax.set_xticks([])
    axs[0].set_ylabel(ylab,fontsize=12)
    handles=[plt.Line2D([0],[0],color=cols[v],lw=3) for v in lv]
    fig.legend(handles,lv,loc='lower center',ncol=len(lv),fontsize=9,frameon=False)
    fig.text(.99,.01,'black line: grand mean',ha='right',fontsize=8)
    fig.tight_layout(rect=(0,.08,1,1)); fig.savefig('bank_images/'+fname)
def crabs_plot():
    c=pd.read_csv('../crabs.csv'); rng=np.random.default_rng(4); lv=sorted(c.crabType.unique())
    fig,ax=plt.subplots(figsize=(7,4.5),dpi=150); pal=['#E8746B','#55B04B','#6A9BF4','#C77CFF']
    for k,(t,col) in enumerate(zip(lv,pal)):
        v=c[c.crabType==t].bodyTemperature; ax.scatter(k+rng.uniform(-.2,.2,len(v)),v,color=col,alpha=.7,s=30); _ci(ax,k,v)
    ax.set_xticks(range(4)); ax.set_xticklabels(lv,fontsize=10); ax.set_ylabel('rate of heat gain (bodyTemperature)',fontsize=11); ax.grid(axis='y',alpha=.35)
    ax.set_title('Points: crabs. Black: mean ± 95% CI',fontsize=10); fig.tight_layout(); fig.savefig('bank_images/ch18-book-crabs.png')
if __name__=='__main__':
    crabs_plot()
    dev_generic(pd.read_csv('../crabs.csv'),'bodyTemperature','crabType',['error','total','model'],['a','b','c'],'ch18-book-crab-deviations.png','bodyTemperature')
    dev_generic(pd.read_csv('../cuckooeggs.csv'),'egg_length','host_species',['model','error','total'],['A','B','C'],'ch18-hw-cuckoo-deviations.png','egg length (mm)')

def ril_pinkGC():
    r=pd.read_csv('../mr_data/rils.csv'); return r[(r.petal_color=='pink')&(r.location=='GC')].dropna(subset=['mean_visits','prop_hybrid']).reset_index(drop=True)
def reg_figs():
    from scipy import stats
    d=ril_pinkGC(); m=smf.ols('prop_hybrid ~ mean_visits',d).fit(); rng=np.random.default_rng(5)
    fig,ax=plt.subplots(figsize=(6,4.5),dpi=150)
    ax.scatter(d.mean_visits+rng.uniform(-.03,.03,len(d)),d.prop_hybrid+rng.uniform(-.01,.01,len(d)),alpha=.6,color='#444',s=30)
    xs=np.linspace(0,d.mean_visits.max(),100); pr=m.get_prediction(pd.DataFrame({'mean_visits':xs})).summary_frame(alpha=.05)
    ax.fill_between(xs,pr.mean_ci_lower,pr.mean_ci_upper,color='grey',alpha=.35); ax.plot(xs,pr['mean'],color='#1f5fbf',lw=2.5)
    ax.set_xlabel('visits (mean pollinator visits per observation)',fontsize=11); ax.set_ylabel('prop_hybrid',fontsize=12)
    ax.set_xticks(np.arange(0,2.01,.25)); ax.set_yticks(np.arange(0,1.01,.1)); ax.grid(alpha=.35)
    fig.tight_layout(); fig.savefig('bank_images/ch19-book-regression.png')
    inf=m.get_influence(); fit=m.fittedvalues.values; res=m.resid.values; sr=inf.resid_studentized_internal; lev=inf.hat_matrix_diag; ck=inf.cooks_distance[0]
    lab_r=np.argsort(-np.abs(res))[:3]; lab_c=np.argsort(-ck)[:3]
    fig,axs=plt.subplots(1,4,figsize=(15,3.8),dpi=150)
    ax=axs[0]; ax.scatter(fit,res,s=18,color='#444'); ax.axhline(0,ls='--',color='grey'); ax.set_title('Residuals vs Fitted'); ax.set_xlabel('Fitted values'); ax.set_ylabel('Residuals')
    for i in lab_r: ax.annotate(str(i+1),(fit[i],res[i]),fontsize=9,color='#C00')
    ax=axs[1]; (osm,osr),(sl,ic,_)=stats.probplot(sr); order=np.argsort(sr); ax.scatter(osm,osr,s=18,color='#444'); ax.plot(osm,ic+sl*osm,'--',color='grey'); ax.set_title('Normal Q-Q'); ax.set_xlabel('Theoretical quantiles'); ax.set_ylabel('Std. residuals')
    for k,i in enumerate(order):
        if i in lab_r: ax.annotate(str(i+1),(osm[k],osr[k]),fontsize=9,color='#C00')
    ax=axs[2]; y=np.sqrt(np.abs(sr)); ax.scatter(fit,y,s=18,color='#444'); ax.set_title('Scale-Location'); ax.set_xlabel('Fitted values'); ax.set_ylabel('√|Std. residuals|')
    for i in lab_r: ax.annotate(str(i+1),(fit[i],y[i]),fontsize=9,color='#C00')
    ax=axs[3]; ax.scatter(lev,sr,s=18,color='#444'); ax.axhline(0,ls='--',color='grey'); ax.set_title('Residuals vs Leverage'); ax.set_xlabel('Leverage'); ax.set_ylabel('Std. residuals')
    for i in lab_c: ax.annotate(str(i+1),(lev[i],sr[i]),fontsize=9,color='#C00')
    fig.tight_layout(); fig.savefig('bank_images/ch19-book-diagnostics.png')
    d['fit']=fit; gm=d.prop_hybrid.mean(); kinds={'total':('prop_hybrid',None),'error':('prop_hybrid','fit'),'model':('fit',None)}
    fig,axs=plt.subplots(1,3,figsize=(12,3.8),dpi=150,sharey=True)
    for ax,k,lab in zip(axs,['total','error','model'],['A','B','C']):
        a,b=kinds[k]; top=d[a]; bot=d[b] if b else np.full(len(d),gm)
        ax.vlines(d.mean_visits,top,bot,color='#D95F9E',lw=1); ax.scatter(d.mean_visits,d.prop_hybrid,s=12,color='#444',zorder=3)
        ax.axhline(gm,color='black',lw=1.2); ax.plot(xs,m.params.iloc[0]+m.params.iloc[1]*xs,color='#1f5fbf',lw=2)
        ax.set_title(lab,fontsize=14,weight='bold'); ax.set_xlabel('visits')
    axs[0].set_ylabel('prop_hybrid'); fig.text(.99,.01,'black: mean prop_hybrid; blue: regression line',ha='right',fontsize=8)
    fig.tight_layout(rect=(0,.03,1,1)); fig.savefig('bank_images/ch19-book-deviations.png')
if __name__=='__main__':
    reg_figs()

def scatter_ci(d,x,y,fname,xlab,ylab):
    m=smf.ols(f'{y} ~ {x}',d).fit(); fig,ax=plt.subplots(figsize=(6,4.5),dpi=150)
    ax.scatter(d[x],d[y],alpha=.6,color='#444',s=30); xs=np.linspace(d[x].min(),d[x].max(),100)
    pr=m.get_prediction(pd.DataFrame({x:xs})).summary_frame(alpha=.05)
    ax.fill_between(xs,pr.mean_ci_lower,pr.mean_ci_upper,color='grey',alpha=.35); ax.plot(xs,pr['mean'],color='#1f5fbf',lw=2.5)
    ax.set_xlabel(xlab,fontsize=12); ax.set_ylabel(ylab,fontsize=12); ax.grid(alpha=.35); fig.tight_layout(); fig.savefig('bank_images/'+fname)
def diag4(d,x,y,fname):
    from scipy import stats
    m=smf.ols(f'{y} ~ {x}',d).fit(); inf=m.get_influence(); fit=m.fittedvalues.values; res=m.resid.values; sr=inf.resid_studentized_internal; lev=inf.hat_matrix_diag
    fig,axs=plt.subplots(1,4,figsize=(15,3.8),dpi=150)
    axs[0].scatter(fit,res,s=18,color='#444'); axs[0].axhline(0,ls='--',color='grey'); axs[0].set_title('Residuals vs Fitted'); axs[0].set_xlabel('Fitted values'); axs[0].set_ylabel('Residuals')
    (osm,osr),(sl,ic,_)=stats.probplot(sr); axs[1].scatter(osm,osr,s=18,color='#444'); axs[1].plot(osm,ic+sl*osm,'--',color='grey'); axs[1].set_title('Normal Q-Q'); axs[1].set_xlabel('Theoretical quantiles'); axs[1].set_ylabel('Std. residuals')
    axs[2].scatter(fit,np.sqrt(np.abs(sr)),s=18,color='#444'); axs[2].set_title('Scale-Location'); axs[2].set_xlabel('Fitted values'); axs[2].set_ylabel('√|Std. residuals|')
    axs[3].scatter(lev,sr,s=18,color='#444'); axs[3].axhline(0,ls='--',color='grey'); axs[3].set_title('Residuals vs Leverage'); axs[3].set_xlabel('Leverage'); axs[3].set_ylabel('Std. residuals')
    fig.tight_layout(); fig.savefig('bank_images/'+fname)
def reg_dev(d,x,y,order,labels,fname,n=None,seed=1):
    m=smf.ols(f'{y} ~ {x}',d).fit(); d=d.copy(); d['fit']=m.fittedvalues
    if n: d=d.sample(n,random_state=seed)
    gm=d[y].mean() if not n else m.model.endog.mean()
    kinds={'total':(y,None),'error':(y,'fit'),'model':('fit',None)}; xs=np.linspace(d[x].min(),d[x].max(),50)
    fig,axs=plt.subplots(1,3,figsize=(12,3.8),dpi=150,sharey=True)
    for ax,k,lab in zip(axs,order,labels):
        a,b=kinds[k]; bot=d[b] if b else np.full(len(d),gm)
        ax.vlines(d[x],d[a],bot,color='#D95F9E',lw=1.2); ax.scatter(d[x],d[y],s=14,color='#444',zorder=3)
        ax.axhline(gm,color='black',lw=1.2); ax.plot(xs,m.params.iloc[0]+m.params.iloc[1]*xs,color='#1f5fbf',lw=2)
        ax.set_title(lab,fontsize=14,weight='bold'); ax.set_xlabel(x)
    axs[0].set_ylabel(y); fig.text(.99,.01,f'black: mean {y}; blue: regression line',ha='right',fontsize=8)
    fig.tight_layout(rect=(0,.03,1,1)); fig.savefig('bank_images/'+fname)
if __name__=='__main__':
    l=pd.read_csv('src/lizardbite.csv').rename(columns={'territory.area':'territory'})
    scatter_ci(l,'bite','territory','ch19-quiz-lizard.png','bite force (N)','territory area (m²)'); diag4(l,'bite','territory','ch19-quiz-lizard-diag.png')
    r=pd.read_csv('../mr_data/rils.csv'); sr=r[r.location=='SR'].dropna(subset=['petal_area_mm','prop_hybrid'])
    scatter_ci(sr,'petal_area_mm','prop_hybrid','ch19-hw-sr.png','petal area (mm²)','prop_hybrid'); diag4(sr,'petal_area_mm','prop_hybrid','ch19-hw-sr-diag.png')
    reg_dev(sr,'petal_area_mm','prop_hybrid',['error','total','model'],['A','B','C'],'ch19-hw-sr-deviations.png',n=30)

def two_slopes(d,x,y,g,fname,xlab,ylab,labels=('A','B'),pal=None,which='both'):
    lv=sorted(d[g].unique()); pal=pal or ['#E8746B','#55B04B','#6A9BF4']; cols=dict(zip(lv,pal))
    add=smf.ols(f'{y} ~ {x} + C({g})',d).fit()
    panels=[('sep',labels[0]),('add',labels[1])] if which=='both' else [(which,None)]
    fig,axs=plt.subplots(1,len(panels),figsize=(5.2*len(panels),4.2),dpi=150,squeeze=False)
    for ax,(kind,lab) in zip(axs[0],panels):
        for v in lv:
            s=d[d[g]==v]; ax.scatter(s[x],s[y],s=20,alpha=.6,color=cols[v],label=v); xs=np.linspace(s[x].min(),s[x].max(),30)
            if kind=='sep': b=np.polyfit(s[x],s[y],1); ax.plot(xs,np.polyval(b,xs),color=cols[v],lw=2.5)
            else: ax.plot(xs,add.predict(pd.DataFrame({x:xs,g:v})),color=cols[v],lw=2.5)
        if lab: ax.set_title(lab,fontsize=14,weight='bold')
        ax.set_xlabel(xlab,fontsize=11); ax.set_ylabel(ylab,fontsize=11); ax.grid(alpha=.3)
    axs[0][-1].legend(title=g,fontsize=9); fig.tight_layout(); fig.savefig('bank_images/'+fname)
def diag_rows(models,names,fname):
    from scipy import stats
    fig,axs=plt.subplots(len(models),4,figsize=(15,3.5*len(models)),dpi=150,squeeze=False)
    for row,(m,nm) in zip(axs,zip(models,names)):
        inf=m.get_influence(); fit=m.fittedvalues.values; res=m.resid.values; sr=inf.resid_studentized_internal; lev=inf.hat_matrix_diag
        row[0].scatter(fit,res,s=14,color='#444'); row[0].axhline(0,ls='--',color='grey'); row[0].set_title(f'{nm}: Residuals vs Fitted',fontsize=10)
        (osm,osr),(sl,ic,_)=stats.probplot(sr); row[1].scatter(osm,osr,s=14,color='#444'); row[1].plot(osm,ic+sl*osm,'--',color='grey'); row[1].set_title(f'{nm}: Normal Q-Q',fontsize=10)
        row[2].scatter(fit,np.sqrt(np.abs(sr)),s=14,color='#444'); row[2].set_title(f'{nm}: Scale-Location',fontsize=10)
        row[3].scatter(lev,sr,s=14,color='#444'); row[3].axhline(0,ls='--',color='grey'); row[3].set_title(f'{nm}: Residuals vs Leverage',fontsize=10)
    fig.tight_layout(); fig.savefig('bank_images/'+fname); plt.close('all')
if __name__=='__main__':
    i=pd.read_csv('../peng/iris.csv'); two_slopes(i,'sepal_length','petal_length','species','ch20-book-iris-slopes.png','Sepal.Length','Petal.Length')
    r=pd.read_csv('../mr_data/rils.csv'); d=r[r.location=='SR'].dropna(subset=['mean_visits','petal_area_mm','asd_mm']).copy(); d['log1p_visits']=np.log1p(d.mean_visits)
    diag_rows([smf.ols('mean_visits ~ petal_area_mm + asd_mm',d).fit(),smf.ols('log1p_visits ~ petal_area_mm + asd_mm',d).fit()],['Model 1 (mean_visits)','Model 2 (log1p_visits)'],'ch20-hw-sr-diag.png')
    mr=pd.read_csv('src/molerats.csv'); two_slopes(mr,'lnMass','lnEnergy','caste','ch20-chimein-molerat-sep.png','lnMass','lnEnergy',pal=['#6A9BF4','#E8746B'],which='sep')
    diag_rows([smf.ols('lnEnergy ~ caste + lnMass',mr).fit()],['lnEnergy ~ caste + lnMass'],'ch20-chimein-molerat-diag.png')

def peng_strip(y,fname,ylab,lines=False):
    p=pd.read_csv('../peng/p.csv').dropna(subset=['sex',y]); rng=np.random.default_rng(8)
    sp=['Adelie','Chinstrap','Gentoo']; cols=dict(zip(sp,['#E8746B','#55B04B','#6A9BF4'])); off=dict(zip(sp,[-.25,0,.25]))
    fig,ax=plt.subplots(figsize=(6,4.5),dpi=150)
    for s in sp:
        mx=[]
        for k,sx in enumerate(['female','male']):
            v=p[(p.species==s)&(p.sex==sx)][y]; ax.scatter(k+off[s]+rng.uniform(-.07,.07,len(v)),v,s=14,alpha=.5,color=cols[s],label=s if k==0 else None)
            mx.append((k+off[s],v.mean()))
        if lines:
            ax.plot([a for a,_ in mx],[b for _,b in mx],color=cols[s],lw=2.5); ax.scatter([a for a,_ in mx],[b for _,b in mx],s=90,color=cols[s],edgecolor='black',zorder=4)
    ax.set_xticks([0,1]); ax.set_xticklabels(['female','male'],fontsize=12); ax.set_ylabel(ylab,fontsize=12); ax.legend(title='species',fontsize=9); ax.grid(axis='y',alpha=.3)
    fig.tight_layout(); fig.savefig('bank_images/'+fname); plt.close('all')
def gc_four():
    r=pd.read_csv('../mr_data/rils.csv'); d=r[(r.location=='GC')&r.petal_color.notna()].dropna(subset=['prop_hybrid','petal_area_mm'])
    cols={'pink':'#D95F9E','white':'#888'}; xs=np.linspace(d.petal_area_mm.min(),d.petal_area_mm.max(),50)
    specs=[('A','prop_hybrid ~ petal_area_mm'),('B','prop_hybrid ~ petal_area_mm * petal_color'),('C','prop_hybrid ~ petal_area_mm + petal_color'),('D','prop_hybrid ~ petal_color')]
    fig,axs=plt.subplots(1,4,figsize=(16,3.8),dpi=150,sharey=True)
    for ax,(lab,f) in zip(axs,specs):
        m=smf.ols(f,d).fit()
        for c,g in d.groupby('petal_color'):
            ax.scatter(g.petal_area_mm,g.prop_hybrid,s=14,alpha=.5,color=cols[c],label=c)
            ax.plot(xs,m.predict(pd.DataFrame({'petal_area_mm':xs,'petal_color':c})),color=cols[c] if 'color' in f else 'black',lw=2.5)
        ax.set_title(lab,fontsize=14,weight='bold'); ax.set_xlabel('petal_area_mm')
    axs[0].set_ylabel('prop_hybrid'); axs[-1].legend(title='petal_color',fontsize=8)
    fig.tight_layout(); fig.savefig('bank_images/ch21-hw-four-models.png')
    diag_rows([smf.ols('prop_hybrid ~ petal_area_mm * petal_color',d).fit()],['prop_hybrid ~ petal_area_mm * petal_color'],'ch21-hw-diag.png')
if __name__=='__main__':
    peng_strip('body_mass_g','ch21-book-mass-sex-species.png','body_mass (g)',lines=True)
    peng_strip('bill_length_mm','ch21-chimein-bill-sex-species.png','bill_len (mm)')
    i=pd.read_csv('../peng/iris.csv')
    two_slopes(i,'petal_width','petal_length','species','ch21-chimein-iris-petal.png','Petal.Width','Petal.Length',which='sep')
    two_slopes(i,'sepal_width','sepal_length','species','ch21-chimein-iris-sepal.png','Sepal.Width','Sepal.Length',which='sep')
    gc_four()
def olympics():
    d=pd.read_csv('src/long_olympics.csv'); cols={'female':'#E8746B','male':'#6A9BF4'}
    fig,ax=plt.subplots(figsize=(6,4.2),dpi=150)
    for g in ['female','male']:
        s=d[d.Gender==g]; ax.scatter(s.Year,s.Time,s=28,alpha=.8,color=cols[g],label=g)
    ax.set_xlabel('Year',fontsize=12); ax.set_ylabel('Winning time, 100 m (seconds)',fontsize=12)
    ax.legend(title='Gender'); ax.grid(alpha=.3); fig.tight_layout(); fig.savefig('bank_images/ch21-quiz-olympics.png'); plt.close('all')
if __name__=='__main__' and 'olympics' in sys.argv: olympics()
