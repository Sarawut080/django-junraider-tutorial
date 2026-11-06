# -*- coding: utf-8 -*-
import html,re,os
OUT=r"D:\DocumentMaster's Degree\05_งานอื่น\django-junraider-tutorial"
CHAPTERS=[(1,"การติดตั้งและเริ่มรันโปรเจกต์ (Setup and Run)"),(2,"โปรเจกต์และแอปพลิเคชัน (Projects x Apps)"),(3,"เส้นทางและวิว (urls x views)"),(4,"วิวและเทมเพลต (views x templates)"),(5,"แท็กในเทมเพลต (templates x tags)"),(6,"ตัวกรองในเทมเพลต (templates x filters)"),(7,"โมเดลและไมเกรชัน (models x migrations)"),(8,"โมเดล (models)"),(9,"โมเดล วิว และเทมเพลต"),(10,"แบบฟอร์ม วิว และเทมเพลต (forms)"),(11,"หน้าผู้ดูแลระบบ (admin)"),(12,"ไฟล์ภาพแบบคงที่ (static images)"),(13,"ไฟล์ CSS และ JavaScript แบบคงที่"),(14,"การตั้งค่าและไฟล์ .env (settings x dotenv)"),(15,"การนำขึ้นใช้งานจริง (Deploy)")]
DONE=set()
def e(s): return html.escape(s,quote=False)
def inl(s):
    parts=re.split(r"(`[^`]+`)",s)
    return "".join("<code>%s</code>"%e(p[1:-1]) if p.startswith("`") and p.endswith("`") and len(p)>2 else p for p in parts)
def p(s): return "<p>%s</p>\n"%inl(s)
def h2(s): return "<h2>%s</h2>\n"%inl(s)
def h3(s): return "<h3>%s</h3>\n"%inl(s)
REPO="https://github.com/potchangelo/django-junraider"
BRANCH={1:"01-setup",2:"02-project-apps",3:"03-urls-views",4:"04-views-templates",5:"05-templates-tags",6:"06-templates-filters",7:"07-models-migrations",8:"08-models",9:"09-models-views-templates",10:"10-forms-views-templates",11:"11-admin",12:"12-static-images",13:"13-static-css-js",14:"14-settings-dotenv",15:"15-deploy-heroku"}
def code(loc,text,copy=True,url=None):
    text=text.rstrip("\n")
    b='<button type="button">คัดลอก</button>' if copy else ""
    lab='<a href="%s" target="_blank" rel="noopener">%s</a>'%(url,e(loc)) if url else e(loc)
    return '<figure class="code"><figcaption><span>%s</span>%s</figcaption><pre><code>%s</code></pre></figure>\n'%(lab,b,e(text))
def outp(label,text):
    return '<figure class="code out"><figcaption><span>%s</span></figcaption><pre><code>%s</code></pre></figure>\n'%(e(label),e(text.rstrip("\n")))
def exp(rows,h1="โค้ด / คำสั่ง",h2_="คำอธิบาย"):
    s='<table class="exp"><thead><tr><th>%s</th><th>%s</th></tr></thead><tbody>\n'%(h1,h2_)
    for a,b in rows: s+="<tr><td><code>%s</code></td><td>%s</td></tr>\n"%(e(a),inl(b))
    return s+"</tbody></table>\n"
def ul(items): return "<ul>\n"+"".join("<li>%s</li>\n"%inl(i) for i in items)+"</ul>\n"
def sidebar(cur):
    s='<nav class="side"><a class="site" href="index.html">สื่อการสอน Django<br>(อ้างอิง django-junraider)</a><ul>'
    s+='<li class="%s"><a href="index.html">หน้าแรก (สารบัญ)</a></li>'%("cur" if cur=="index" else "")
    s+='</ul><h4>บทเรียน (Season 1)</h4><ul>'
    for n,t in CHAPTERS:
        if n in DONE: s+='<li class="%s"><a href="ch%02d.html">บทที่ %d %s</a></li>'%("cur" if cur==n else "",n,n,e(t))
        else: s+='<li class="off">บทที่ %d %s</li>'%(n,e(t))
    s+='</ul><ul><li class="%s"><a href="credits.html">ที่มา (Credits)</a></li></ul></nav>'%("cur" if cur=="credits" else "")
    return s
def pager(n):
    prev=('<a href="ch%02d.html">&larr; บทก่อนหน้า: บทที่ %d</a>'%(n-1,n-1)) if n-1 in DONE else ('<a href="index.html">&larr; หน้าแรก</a>' if n==1 else '<span></span>')
    nxt=('<a href="ch%02d.html">บทถัดไป: บทที่ %d &rarr;</a>'%(n+1,n+1)) if n+1 in DONE else '<span></span>'
    return '<div class="pager">%s%s</div>'%(prev,nxt)
def page(fname,title,cur,body,n=None):
    h='<!DOCTYPE html>\n<html lang="th">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>%s</title>\n<link rel="stylesheet" href="style.css">\n</head>\n<body>\n<div class="layout">\n%s\n<main>\n%s%s</main>\n</div>\n<script src="script.js"></script>\n</body>\n</html>\n'%(e(title),sidebar(cur),body,pager(n) if n else "")
    open(os.path.join(OUT,fname),"w",encoding="utf-8",newline="\n").write(h)
def chapter(n,body):
    t=dict(CHAPTERS)[n]
    br=BRANCH[n]
    ref='<p class="ref">อ้างอิง GitHub: <a href="%s/tree/%s" target="_blank" rel="noopener">บรานช์ %s</a> · <a href="%s/compare/%s...%s" target="_blank" rel="noopener">ส่วนที่เปลี่ยนจากบทก่อนหน้า</a></p>\n'%(REPO,br,br,REPO,BRANCH[n-1],br) if n>1 else '<p class="ref">อ้างอิง GitHub: <a href="%s/tree/%s" target="_blank" rel="noopener">บรานช์ %s</a></p>\n'%(REPO,br,br)
    page("ch%02d.html"%n,"บทที่ %d %s"%(n,t),n,'<p class="ch">บทที่ %d จาก 15</p>\n<h1>%s</h1>\n'%(n,e(t))+ref+body,n)
def rurl(n,path): return "%s/blob/%s/%s"%(REPO,BRANCH[n],path)
