# -*- coding: utf-8 -*-
"""Static site generator for Yunus Abdulsalam SAN & Co."""
import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set this to the firm's real domain before launch (no trailing slash),
# e.g. "https://www.yunusabdulsalamsan.com" — then rebuild.
SITE_URL = "https://yaslegal.org"

LOGO_SVG = """<svg viewBox="0 0 64 64" role="img" aria-label="Yunus Abdulsalam SAN &amp; Co. monogram"><circle cx="32" cy="32" r="27" fill="none" stroke="{c}" stroke-width="3.4"/><path d="M20 18 L32 34 L44 18" fill="none" stroke="{c}" stroke-width="3.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M32 34 L32 46" fill="none" stroke="{c}" stroke-width="3.8" stroke-linecap="round"/><path d="M45 20 L21 47" fill="none" stroke="#b08d3f" stroke-width="3.4" stroke-linecap="round"/></svg>"""

NAV = [("index.html","Home"),("about.html","The Firm"),("practice-areas.html","Practice Areas"),
       ("team.html","Our Team"),("publications.html","Publications"),("contact.html","Contact")]


def logo(light=False):
    c = "#ffffff" if light else "#13315c"
    cls = "logo logo--light" if light else "logo"
    return f"""<a class="{cls}" href="index.html" aria-label="{FIRM} home">
      {LOGO_SVG.format(c=c)}
      <span class="logo-text">
        <span class="logo-name">Yunus Abdulsalam <span class="san">SAN &amp; CO.</span></span>
        <span class="logo-tag">{TAG}</span>
      </span>
    </a>"""


def mini_card(name, role, photo):
    if photo:
        ph = f'<span class="mini-photo"><img src="assets/img/team/{photo}" alt="{name}, {role}" loading="lazy" width="480" height="480"></span>'
    else:
        ph = f'<span class="mini-photo mini-initials">{initials(name)}</span>'
    return f"""      <a class="mini" href="team.html">
        {ph}
        <span class="mini-name">{name}</span>
        <span class="mini-role">{role}</span>
      </a>
"""


def ico(slug, cls="ico"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[slug]}</svg>'


def vico(i):
    return f'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{VALUE_ICONS[i % len(VALUE_ICONS)]}</svg>'


def val_cards(items, offset=0):
    return "".join(
        f"""      <div class="value-card"><span class="value-ico">{vico(i+offset)}</span><h3>{n}</h3><p style="font-size:.95rem;margin:0">{d}</p></div>\n"""
        for i,(n,d) in enumerate(items))


def jsonld(active):
    firm = {
        "@context": "https://schema.org",
        "@type": "LegalService",
        "name": "Yunus Abdulsalam SAN & Co.",
        "alternateName": "Yunus Abdulsalam SAN and Co",
        "description": "Full-service Nigerian law firm in Asokoro, Abuja — debt recovery, property law, litigation, arbitration, energy law and corporate practice.",
        "url": SITE_URL + "/",
        "telephone": PHONE.replace(" ", ""),
        "email": EMAIL,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Flat D2, Hampton Apartment, No. 2 Mungo Park Close, Off Jesse Jackson Street",
            "addressLocality": "Asokoro, Abuja",
            "addressRegion": "Federal Capital Territory",
            "addressCountry": "NG",
        },
        "areaServed": "Nigeria",
        "founder": {"@type": "Person", "name": "Yunus Abdulsalam", "honorificSuffix": "SAN", "jobTitle": "Principal Partner"},
        "knowsAbout": [t.replace("&amp;", "&") for _, t, _, _ in AREAS],
        "openingHours": "Mo-Fr 09:00-17:00",
    }
    blocks = [firm]
    crumb_titles = {
        "about.html": "The Firm", "practice-areas.html": "Practice Areas",
        "team.html": "Our Team", "publications.html": "Publications",
        "contact.html": "Contact", "yunus-abdulsalam.html": "Yunus Abdulsalam, SAN",
    }
    if active in crumb_titles:
        blocks.append({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
                {"@type": "ListItem", "position": 2, "name": crumb_titles[active],
                 "item": SITE_URL + "/" + active},
            ],
        })
    if active == "team.html" or active == "yunus-abdulsalam.html":
        blocks.append({
            "@context": "https://schema.org",
            "@type": "Person",
            "name": "Yunus Abdulsalam",
            "honorificSuffix": "SAN",
            "jobTitle": "Principal Partner, Yunus Abdulsalam SAN & Co.",
            "url": SITE_URL + "/yunus-abdulsalam.html",
            "image": SITE_URL + "/assets/img/yunus-abdulsalam-full.jpg",
            "alumniOf": ["Bayero University, Kano", "University of Lincoln", "Nigerian Law School"],
            "memberOf": ["Nigerian Bar Association", "African Bar Association"],
            "worksFor": {"@type": "LegalService", "name": "Yunus Abdulsalam SAN & Co."},
        })
    import json as _json
    return "\n".join(
        '<script type="application/ld+json">' + _json.dumps(b, ensure_ascii=False) + "</script>"
        for b in blocks)


def head(title, desc, active):
    ACT = ' class="active"'
    nav = "\n        ".join(
        '<a href="%s"%s>%s</a>' % (h, ACT if h == active else "", t) for h, t in NAV)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | {FIRM}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#13315c">
<meta property="og:title" content="{title} | {FIRM}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Yunus Abdulsalam SAN &amp; Co.">
<meta property="og:locale" content="en_NG">
<meta property="og:url" content="{SITE_URL}/{active if active != 'index.html' else ''}">
<meta property="og:image" content="{SITE_URL}/assets/img/og-card.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Yunus Abdulsalam SAN &amp; Co., Legal Practitioners and Arbitrators, Asokoro, Abuja">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title} | {FIRM}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE_URL}/assets/img/og-card.jpg">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="geo.region" content="NG-FC">
<meta name="geo.placename" content="Asokoro, Abuja">
<link rel="canonical" href="{SITE_URL}/{active if active != 'index.html' else ''}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
{jsonld(active)}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>

<div class="topbar">
  <div class="wrap">
    <div class="topbar-items">
      <span class="hide-sm">Asokoro, Abuja &middot; FCT, Nigeria</span>
    </div>
    <div class="topbar-items">
      <a href="tel:{PHONE_HREF}">{PHONE}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
</div>

<header class="site-header">
  <div class="wrap">
    {logo()}
    <button class="burger" id="burger" aria-label="Menu" aria-expanded="false" aria-controls="nav">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav" id="nav">
        {nav}
        <a class="btn btn--nav" href="contact.html">Consultation</a>
    </nav>
  </div>
</header>
"""


FOOT_AREAS = ["debt-recovery","litigation","arbitration","property-law","oil-and-gas","corporate-commercial"]

def foot():
    links = "\n      ".join(f'<li><a href="practice-areas.html#{s}">{t}</a></li>'
                            for s,t,_,_ in AREAS if s in FOOT_AREAS)
    nav = "\n      ".join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV)
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        {logo(light=True)}
        <p>A full-service Nigerian law firm with over 15 years of distinction in debt recovery, property law, litigation and arbitration.</p>
      </div>
      <div>
        <h4>Navigate</h4>
        <ul>
      {nav}
        </ul>
      </div>
      <div>
        <h4>Key Practices</h4>
        <ul>
      {links}
          <li><a href="practice-areas.html">View all 21 &rarr;</a></li>
        </ul>
      </div>
      <div>
        <h4>Head Office</h4>
        <ul>
          <li>{ADDR_L1}</li>
          <li>{ADDR_L2}</li>
          <li><a href="tel:{PHONE_HREF}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 {FIRM} All rights reserved.</span>
      <span>Legal Practitioners &amp; Arbitrators &middot; Abuja, Nigeria</span>
    </div>
  </div>
  <div class="disclaimer">
    <div class="wrap">
      This website is provided for general information only and does not constitute legal advice, nor does it create a lawyer&ndash;client relationship. In compliance with the Rules of Professional Conduct for Legal Practitioners in Nigeria, no part of this site is intended as an advertisement or solicitation. Please contact the firm directly for advice on your specific circumstances.
    </div>
  </div>
</footer>

<script>
(function(){{
  var b=document.getElementById('burger'), n=document.getElementById('nav');
  if(b&&n){{
    b.addEventListener('click',function(){{
      var open=n.classList.toggle('open');
      b.setAttribute('aria-expanded',open?'true':'false');
      document.body.style.overflow=open?'hidden':'';
    }});
    n.addEventListener('click',function(e){{
      if(e.target.tagName==='A'){{n.classList.remove('open');b.setAttribute('aria-expanded','false');document.body.style.overflow='';}}
    }});
  }}
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var els = document.querySelectorAll('.reveal, .card, .value-card, .person, .pub-item, .fact, .stat');
  if (reduce || !('IntersectionObserver' in window)) {{
    for (var i=0;i<els.length;i++) els[i].classList.add('is-in');
  }} else {{
    for (var j=0;j<els.length;j++) els[j].classList.add('will-reveal');
    var io = new IntersectionObserver(function(entries){{
      entries.forEach(function(en){{
        if (en.isIntersecting) {{ en.target.classList.add('is-in'); io.unobserve(en.target); }}
      }});
    }}, {{ rootMargin: '0px 0px -40px 0px', threshold: 0.06 }});
    for (var k=0;k<els.length;k++) io.observe(els[k]);
  }}
  var f=document.getElementById('enquiry');
  if(f){{
    f.addEventListener('submit',function(e){{
      e.preventDefault();
      var d=new FormData(f);
      var body='Name: '+d.get('name')+'%0D%0APhone: '+d.get('phone')
        +'%0D%0AArea of interest: '+d.get('area')+'%0D%0A%0D%0A'+encodeURIComponent(d.get('message')||'');
      window.location.href='mailto:{EMAIL}?subject='
        +encodeURIComponent('Website enquiry — '+(d.get('name')||''))+'&body='+body;
      document.getElementById('formStatus').textContent='Opening your email client…';
    }});
  }}
}})();
</script>
</body>
</html>
"""


def cta(title="Speak With Our Lawyers", text="Tell us about your matter. We will respond with a clear view of your options and the next steps."):
    return f"""
<section class="cta">
  <div class="wrap">
    <span class="eyebrow" style="color:var(--gold-light)">Get in touch</span>
    <h2>{title}</h2>
    <p>{text}</p>
    <a class="btn" href="contact.html">Request a Consultation</a>
    <a class="btn btn--light" href="tel:{PHONE_HREF}" style="margin-left:10px">{PHONE}</a>
  </div>
</section>
"""


def pagehead(title, sub, crumb):
    return f"""
<section class="pagehead">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; {crumb}</div>
    <h1>{title}</h1>
    <p>{sub}</p>
  </div>
</section>
"""


def initials(name):
    parts = [p for p in name.replace(".", " ").split() if p]
    return (parts[0][0] + parts[-1][0]).upper()


def person_card(name, role, photo, link=None, lead=False):
    if photo:
        av = f'<div class="avatar avatar--photo"><img src="assets/img/team/{photo}" alt="{name}, {role}" loading="lazy" width="480" height="480"></div>'
    else:
        av = f'<div class="avatar" aria-hidden="true">{initials(name)}</div>'
    inner = f'{av}<h3>{name}</h3><p class="role">{role}</p>'
    cls = "person person--lead" if lead else "person"
    if link:
        inner += '<p class="card-more" style="margin-top:14px">Read full profile &rarr;</p>'
        return f'<a class="person-link" href="{link}"><div class="{cls}">{inner}</div></a>'
    return f'<div class="{cls}">{inner}</div>'


# ============================================================== HOME
def page_home():
    feat = ["debt-recovery","litigation","arbitration","property-law","oil-and-gas","corporate-commercial"]
    cards = ""
    import re as _re
    def _snippet(text, min_len=70):
        parts = _re.split(r'(?<=\.)\s+', text.strip())
        out = ""
        for p in parts:
            out = (out + " " + p).strip()
            if len(out) >= min_len:
                break
        return out.rstrip(".") + "."
    for s,t,paras,_ in AREAS:
        if s in feat:
            snip = _snippet(paras[0])
            cards += f"""      <a class="card" href="practice-areas.html#{s}">
        <span class="card-ico">{ico(s)}</span>
        <h3>{t}</h3><p>{snip}</p>
        <span class="card-more">Learn more &rarr;</span>
      </a>\n"""
    vals = val_cards(VALUES[:3])

    return head("Leading Law Firm in Abuja",
        "Yunus Abdulsalam SAN & Co. is a full-service law firm in Asokoro, Abuja, with over 15 years of distinction in debt recovery, property law, litigation and arbitration.",
        "index.html") + f"""
<section class="hero">
  <div class="hero-chev" aria-hidden="true"></div>
  <div class="wrap hero-in">
    <span class="eyebrow">Legal Practitioners &amp; Arbitrators &middot; Abuja</span>
    <h1>Strategic counsel for Nigeria&rsquo;s most demanding legal matters.</h1>
    <p>A Senior Advocate&ndash;led firm delivering results in debt recovery, property, energy, arbitration and corporate disputes.</p>
    <div class="hero-actions">
      <a class="btn" href="contact.html">Request a Consultation</a>
      <a class="btn btn--light" href="practice-areas.html">Our Practice Areas</a>
    </div>
  </div>
</section>

<section class="stats section--tight">
  <div class="wrap">
    <div class="grid grid-4">
      <div class="stat"><b>15+</b><span>Years of practice</span></div>
      <div class="stat"><b>21</b><span>Practice areas</span></div>
      <div class="stat"><b>SAN</b><span>Senior Advocate led</span></div>
      <div class="stat"><b>&#8358;100s M</b><span>Recovered for clients</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid-2" style="gap:56px;align-items:center">
      <div>
        <span class="eyebrow">The Firm</span>
        <h2>A distinguished practice built on precision and results</h2>
        <hr class="rule">
        <p>For over 15 years, we have delivered excellent legal services across Nigeria &mdash; with particular distinction in debt recovery, property law, litigation, and corporate practice.</p>
        <p>The firm is led by Yunus Abdulsalam, SAN, a respected Senior Advocate of Nigeria whose leadership embodies dedication, precision, and an unwavering commitment to justice.</p>
        <a class="btn btn--ghost" href="about.html">More About the Firm</a>
      </div>
      <div>
        <div class="card" style="border-top-width:4px">
          <span class="eyebrow">Our Mission</span>
          <p style="font-size:1.02rem">Cutting-edge legal solutions anchored on professionalism, innovation, and client-focused advocacy.</p>
          <hr class="rule" style="margin:24px 0 20px">
          <span class="eyebrow">Our Vision</span>
          <p style="font-size:1.02rem;margin-bottom:0">To be a trusted global partner in innovative legal solutions, empowering clients to achieve lasting success.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="center" style="max-width:640px;margin:0 auto 46px">
      <span class="eyebrow">What We Do</span>
      <h2>Practice Areas</h2>
      <hr class="rule rule--center">
      <p class="lead">Twenty-one practice areas. One standard of advocacy.</p>
    </div>
    <div class="grid grid-3">
{cards}    </div>
    <div class="center" style="margin-top:42px">
      <a class="btn btn--ghost" href="practice-areas.html">View All 21 Practice Areas</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap center" style="max-width:760px">
    <span class="eyebrow">Leadership</span>
    <h2>Led by a Senior Advocate of Nigeria</h2>
    <hr class="rule rule--center">
    <span class="lead-portrait reveal">
      <img src="assets/img/yunus-abdulsalam-robe.jpg" alt="Yunus Abdulsalam, SAN, Principal Partner, in Senior Advocate robes" width="880" height="1441" loading="lazy" decoding="async">
    </span>
    <h3 style="font-size:1.5rem;margin-bottom:.15em">Yunus Abdulsalam, SAN</h3>
    <p class="mini-role" style="margin-bottom:18px">Principal Partner</p>
    <p>Founder and Principal Partner Yunus Abdulsalam SAN has recovered debts running into hundreds of millions of naira for AMCON, and was engaged by NNPC in a multimillion-dollar international suit.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:6px">
      <a class="btn" href="yunus-abdulsalam.html">Read More</a>
      <a class="btn btn--ghost" href="team.html">Meet the Team</a>
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="center" style="max-width:620px;margin:0 auto 44px">
      <span class="eyebrow">How We Work</span>
      <h2>Our Values</h2>
      <hr class="rule rule--center">
    </div>
    <div class="grid grid-3">
{vals}    </div>
    <div class="center" style="margin-top:38px"><a class="btn btn--ghost" href="about.html#values">All Six Values</a></div>
  </div>
</section>
""" + cta() + foot()


# ============================================================== ABOUT
def page_about():
    vals = val_cards(VALUES)
    return head("The Firm",
        "Learn about Yunus Abdulsalam SAN & Co. — a distinguished Abuja law firm with over 15 years of excellence in Nigerian legal practice.",
        "about.html") + pagehead("The Firm",
        "Over 15 years of excellence, innovation, and strategic legal solutions tailored to the unique needs of each client.",
        "The Firm") + f"""
<section class="section">
  <div class="wrap" style="max-width:880px">
    <span class="eyebrow">About Us</span>
    <h2>More than legal advisors &mdash; strategic partners</h2>
    <hr class="rule">
    <p class="lead">A distinguished law firm with over 15 years of excellence &mdash; best known for debt recovery, property law, litigation, and corporate practice.</p>
    <p>We serve clients across real estate, banking and finance, corporate and commercial law, and secured credit transactions, delivering results-driven services that meet international best practices while upholding the highest ethics at the Bar.</p>
    <div class="highlight-box">
      <p>The firm is led by Yunus Abdulsalam, SAN, a respected Senior Advocate of Nigeria. We are more than legal advisors &mdash; we are strategic partners who help clients navigate complex challenges with confidence.</p>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="grid grid-2" style="gap:56px">
      <div>
        <span class="eyebrow" style="color:var(--gold-light)">Our Vision</span>
        <h2 style="font-size:1.9rem">Where we are going</h2>
        <hr class="rule">
        <p>To be a trusted global partner in innovative legal solutions, empowering clients to achieve lasting success and sustainable growth.</p>
      </div>
      <div>
        <span class="eyebrow" style="color:var(--gold-light)">Our Mission</span>
        <h2 style="font-size:1.9rem">How we get there</h2>
        <hr class="rule">
        <p>To deliver cutting-edge legal solutions anchored on professionalism, innovation, and client-focused advocacy &mdash; achieving impactful results through diligence and uncompromising ethics.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="values">
  <div class="wrap">
    <div class="center" style="max-width:640px;margin:0 auto 46px">
      <span class="eyebrow">What Guides Us</span>
      <h2>Our Values</h2>
      <hr class="rule rule--center">
      <p class="lead">Six principles behind every engagement.</p>
    </div>
    <div class="grid grid-3">
{vals}    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap center" style="max-width:760px;margin:0 auto">
    <span class="eyebrow">Track Record</span>
    <h2>Recognised where it counts</h2>
    <hr class="rule rule--center">
    <p class="lead">Substantial recoveries for AMCON and commercial banks. Instructed by NNPC in a multimillion-dollar international dispute. Favourable outcomes across Nigeria&rsquo;s trial and appellate courts.</p>
    <a class="btn btn--ghost" href="yunus-abdulsalam.html" style="margin-top:12px">Meet the Principal Partner</a>
  </div>
</section>
""" + cta() + foot()


# ============================================================== PRACTICE AREAS
def page_areas():
    idx = "".join(f'      <a href="#{s}">{ico(s,"ico ico-sm")} {t}</a>\n' for s,t,_,_ in AREAS)
    blocks = ""
    for i,(s,t,paras,bullets) in enumerate(AREAS, 1):
        body = "".join(f"    <p>{p}</p>\n" for p in paras)
        if bullets:
            body += "    <p><strong>Our expertise covers key areas such as:</strong></p>\n    <ul>\n"
            body += "".join(f"      <li><strong>{b}:</strong> {d}</li>\n" for b,d in bullets)
            body += "    </ul>\n"
        blocks += f"""  <div class="pa-block" id="{s}">
    <h2><span class="pa-ico">{ico(s)}</span> {t} <span class="pa-num">{i:02d} / 21</span></h2>
    <hr class="rule">
{body}    <a class="backtop" href="#index">&uarr; Back to all practice areas</a>
  </div>
"""
    return head("Practice Areas",
        "21 practice areas — debt recovery, litigation, arbitration, energy, property, corporate, tax, maritime, IP and more, from Yunus Abdulsalam SAN & Co., Abuja.",
        "practice-areas.html") + pagehead("Practice Areas",
        "Twenty-one areas of practice, spanning dispute resolution, commercial advisory, and Nigeria&rsquo;s most heavily regulated industries.",
        "Practice Areas") + f"""
<section class="section--tight" style="padding-top:52px" id="index">
  <div class="wrap">
    <div class="pa-list">
{idx}    </div>
  </div>
</section>

<section class="section" style="padding-top:20px">
  <div class="wrap" style="max-width:900px">
{blocks}  </div>
</section>
""" + cta("Not sure which practice applies?",
          "Describe your matter and we will point you to the right team &mdash; and the right first step.") + foot()


# ============================================================== TEAM
def page_team():
    cards = "".join("      " + person_card(n, r, p, l) + "\n" for n,r,p,l in TEAM)
    return head("Our Team",
        "Meet the lawyers of Yunus Abdulsalam SAN & Co. — led by Principal Partner Yunus Abdulsalam, SAN.",
        "team.html") + pagehead("Our Team",
        "A team of highly skilled professionals led by a Senior Advocate of Nigeria.",
        "Our Team") + f"""
<section class="section">
  <div class="wrap">
    <span class="eyebrow">Leadership</span>
    <h2>Principal Partner</h2>
    <hr class="rule">
    <div class="profile-lead" style="margin-top:34px">
      <div class="profile-portrait">
        <img src="assets/img/yunus-abdulsalam-full.jpg" alt="Yunus Abdulsalam, SAN, Principal Partner" width="880" height="1579" fetchpriority="high" decoding="async">
        <div class="pp-body">
          <h3>Yunus Abdulsalam, SAN</h3>
          <p class="role">Principal Partner</p>
          <div class="pp-meta"><a href="mailto:{EMAIL_PARTNER}">{EMAIL_PARTNER}</a></div>
        </div>
      </div>
      <div>
        <p class="lead">Senior Advocate of Nigeria, founder and Principal Partner. His practice spans debt recovery, property, litigation, energy law, and constitutional matters.</p>
        <p>He has recovered debts running into hundreds of millions of naira for AMCON, and was engaged by NNPC in a multimillion-dollar international suit.</p>
        <div class="fact-grid">
          <div class="fact">
            <h4>Education</h4>
            <p>Bayero University, Kano &middot; University of Lincoln, UK &middot; Nigerian Law School</p>
          </div>
          <div class="fact">
            <h4>Memberships</h4>
            <p>Senior Advocate of Nigeria &middot; Nigerian Bar Association &middot; African Bar Association</p>
          </div>
          <div class="fact">
            <h4>Core Focus</h4>
            <p>Debt recovery &middot; Litigation &middot; Energy law &middot; Constitutional matters</p>
          </div>
          <div class="fact">
            <h4>Notable</h4>
            <p>AMCON recoveries in the hundreds of millions &middot; NNPC instruction, 2020</p>
          </div>
        </div>
        <a class="btn" href="yunus-abdulsalam.html" style="margin-top:24px">Read His Full Profile</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="center" style="max-width:620px;margin:0 auto 46px">
      <span class="eyebrow">The Practice</span>
      <h2>Associates &amp; Staff</h2>
      <hr class="rule rule--center">
      <p class="lead">Diverse experience across litigation, corporate advisory, and regulated industries.</p>
    </div>
    <div class="grid grid-3">
{cards}    </div>
  </div>
</section>
""" + cta("Work with our team", "Speak to a lawyer about your matter today.") + foot()


# ============================================================== PRINCIPAL BIO
def page_principal():
    return head("Yunus Abdulsalam, SAN — Principal Partner",
        "Profile of Yunus Abdulsalam, SAN, Senior Advocate of Nigeria and Principal Partner of Yunus Abdulsalam SAN & Co., Abuja.",
        "team.html") + pagehead("Yunus Abdulsalam, SAN",
        "Senior Advocate of Nigeria &middot; Founder and Principal Partner",
        '<a href="team.html">Our Team</a> &nbsp;/&nbsp; Yunus Abdulsalam, SAN') + f"""
<section class="section">
  <div class="wrap">
    <div class="profile-lead">
      <div class="profile-portrait">
        <img src="assets/img/yunus-abdulsalam-full.jpg" alt="Yunus Abdulsalam, SAN, Principal Partner" width="880" height="1579" fetchpriority="high" decoding="async">
        <div class="pp-body">
          <h3>Yunus Abdulsalam, SAN</h3>
          <p class="role">Principal Partner</p>
          <div class="pp-meta">
            <a href="mailto:{EMAIL_PARTNER}">{EMAIL_PARTNER}</a><br>
            <a href="tel:{PHONE_HREF}">{PHONE}</a>
          </div>
        </div>
      </div>
      <div class="bio">
        <span class="eyebrow">Profile</span>
        <h2>Senior Advocate of Nigeria</h2>
        <hr class="rule">
        <p class="lead">Yunus Abdulsalam SAN is a Senior Advocate of Nigeria and the founder and Principal Partner of Yunus Abdulsalam SAN &amp; Co.</p>
        <p>With more than a decade of robust practice, he is known for dissecting knotty legal issues with precision &mdash; across debt recovery, property, litigation, energy law, and constitutional matters.</p>

        <h3>Track record</h3>
        <p>He has recovered outstanding debts running into hundreds of millions of naira for AMCON &mdash; including from a former Niger-Delta governor &mdash; and remains a trusted recovery agent for one of the foremost commercial banks in Abuja.</p>

        <div class="highlight-box">
          <p><strong>NNPC instruction, 2020.</strong> Engaged by the Nigerian National Petroleum Commission to defend a multimillion-dollar suit filed by Zhejiang Pufa Group Building Material Limited.</p>
        </div>

        <h3>Areas of focus</h3>
        <ul class="cred-list">
          <li>Debt recovery, asset recovery and secured credit transactions</li>
          <li>Mortgage perfection, conveyancing and perfection of title</li>
          <li>Litigation and civil procedure, from trial courts to the appellate level</li>
          <li>Energy law, oil and gas, and telecommunications</li>
          <li>Constitutional and fundamental rights matters</li>
          <li>Arbitration and alternative dispute resolution</li>
        </ul>

        <h3>Education</h3>
        <ul class="cred-list">
          <li>Bayero University, Kano (BUK)</li>
          <li>University of Lincoln, United Kingdom</li>
          <li>Nigerian Law School</li>
        </ul>

        <h3>Publications</h3>
        <p>He writes on law and public affairs &mdash; see his <a href="publications.html">articles and press coverage</a>.</p>

        <h3>Professional memberships</h3>
        <ul class="cred-list">
          <li>Senior Advocate of Nigeria (SAN)</li>
          <li>Nigerian Bar Association</li>
          <li>African Bar Association</li>
        </ul>

        <p style="margin-top:34px">
          <a class="btn" href="contact.html">Request a Consultation</a>
          <a class="btn btn--ghost" href="team.html" style="margin-left:10px">Back to Our Team</a>
        </p>
      </div>
    </div>
  </div>
</section>
""" + cta() + foot()


# ============================================================== PUBLICATIONS
def pub_item(year, title, outlet, url, desc):
    t = f'<a href="{url}" target="_blank" rel="noopener">{title}</a>' if url else title
    yr = f'<span class="pub-year">{year}</span>' if year else '<span class="pub-year">&mdash;</span>'
    ext = ' <span class="pub-ext">&nearr;</span>' if url else ""
    return f"""      <article class="pub-item">
        {yr}
        <div>
          <h3>{t}{ext}</h3>
          <p class="pub-outlet">{outlet}</p>
          <p class="pub-desc">{desc}</p>
        </div>
      </article>
"""


def page_pubs():
    arts = "".join(pub_item(*p) for p in PUBS_ARTICLES)
    news = "".join(pub_item(*p) for p in PUBS_NEWS)
    return head("Publications",
        "Articles and commentary by Yunus Abdulsalam, SAN, and press coverage of Yunus Abdulsalam SAN & Co.",
        "publications.html") + pagehead("Publications",
        "Legal commentary by the Principal Partner, and coverage of the firm&rsquo;s work in the press.",
        "Publications") + f"""
<section class="section">
  <div class="wrap" style="max-width:880px">
    <span class="eyebrow">Commentary</span>
    <h2>Articles by Yunus Abdulsalam, SAN</h2>
    <hr class="rule">
    <div class="pub-list">
{arts}    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap" style="max-width:880px">
    <span class="eyebrow">Press</span>
    <h2>The Firm in the News</h2>
    <hr class="rule">
    <div class="pub-list">
{news}    </div>
    <p class="muted" style="font-size:.88rem;margin-top:26px">External links open the publisher&rsquo;s website in a new tab. The firm is not responsible for the content of third-party sites.</p>
  </div>
</section>
""" + cta("Have a matter worth writing about?",
          "Speak with our lawyers about representation or a legal opinion.") + foot()


# ============================================================== CONTACT
def page_contact():
    opts = "".join(f'          <option>{t}</option>\n' for _,t,_,_ in AREAS)
    return head("Contact",
        f"Contact Yunus Abdulsalam SAN & Co. — {ADDR_L1}, {ADDR_L2}. Telephone {PHONE}.",
        "contact.html") + pagehead("Contact Us",
        "Tell us about your matter. We will respond with a clear view of your options and the next steps.",
        "Contact") + f"""
<section class="section">
  <div class="wrap">
    <div class="contact-grid">
      <div>
        <span class="eyebrow">Head Office</span>
        <h2>Asokoro, Abuja</h2>
        <hr class="rule">
        <div class="info-item">
          <div class="info-ico" aria-hidden="true">
            <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
          </div>
          <div><h4>Address</h4><p>{ADDR_L1}<br>{ADDR_L2}</p></div>
        </div>
        <div class="info-item">
          <div class="info-ico" aria-hidden="true">
            <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6A19.8 19.8 0 012.1 4.2 2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .4 1.9.7 2.8a2 2 0 01-.5 2.1L8.1 9.9a16 16 0 006 6l1.3-1.2a2 2 0 012.1-.5c.9.3 1.8.6 2.8.7a2 2 0 011.7 2z"/></svg>
          </div>
          <div><h4>Telephone</h4><p><a href="tel:{PHONE_HREF}">{PHONE}</a></p></div>
        </div>
        <div class="info-item">
          <div class="info-ico" aria-hidden="true">
            <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/></svg>
          </div>
          <div><h4>Email</h4><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
        </div>
        <div class="info-item">
          <div class="info-ico" aria-hidden="true">
            <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
          </div>
          <div><h4>Office Hours</h4><p>Monday &ndash; Friday, 9:00am &ndash; 5:00pm (WAT)</p></div>
        </div>
        <div style="margin-top:28px">
          <a class="btn" href="tel:{PHONE_HREF}">Call the Office</a>
          <a class="btn btn--ghost" href="mailto:{EMAIL}" style="margin-left:10px">Send an Email</a>
        </div>
      </div>

      <div>
        <div class="form-card">
          <span class="eyebrow">Enquiry</span>
          <h3 style="font-size:1.4rem">Request a consultation</h3>
          <form id="enquiry" novalidate>
            <div class="field">
              <label for="name">Full name</label>
              <input id="name" name="name" type="text" required placeholder="Your name">
            </div>
            <div class="field">
              <label for="phone">Phone or email</label>
              <input id="phone" name="phone" type="text" required placeholder="How we should reach you">
            </div>
            <div class="field">
              <label for="area">Area of interest</label>
              <select id="area" name="area">
                <option>General enquiry</option>
{opts}              </select>
            </div>
            <div class="field">
              <label for="message">Brief description of your matter</label>
              <textarea id="message" name="message" placeholder="Please do not include confidential details in this first message."></textarea>
            </div>
            <button class="btn" type="submit">Send Enquiry</button>
            <p class="form-status" id="formStatus" role="status"></p>
            <p class="form-note">This form opens your email client with the details pre-filled. Submitting an enquiry does not create a lawyer&ndash;client relationship.</p>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section--tight section--sand">
  <div class="wrap center">
    <span class="eyebrow">Find Us</span>
    <h2 style="font-size:1.6rem">Flat D2, Hampton Apartment, Asokoro</h2>
    <p class="lead" style="max-width:560px;margin:0 auto 22px">No. 2 Mungo Park Close, off Jesse Jackson Street, Asokoro, Abuja &mdash; a short drive from the Central Business District.</p>
    <a class="btn btn--ghost" href="https://www.google.com/maps/search/?api=1&amp;query=2+Mungo+Park+Close+Asokoro+Abuja" target="_blank" rel="noopener">Open in Google Maps</a>
  </div>
</section>
""" + foot()


def page_404():
    return head("Page Not Found",
        "That page could not be found. Browse the practice areas or contact Yunus Abdulsalam SAN & Co. in Asokoro, Abuja.",
        "") + f"""
<section class="section center" style="padding:110px 0">
  <div class="wrap" style="max-width:620px">
    <span class="eyebrow">Error 404</span>
    <h1 style="font-size:clamp(2rem,6vw,3rem)">This page could not be found</h1>
    <hr class="rule rule--center">
    <p class="lead">The page may have been moved or the address mistyped. These links will get you back on track.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:28px">
      <a class="btn" href="index.html">Return Home</a>
      <a class="btn btn--ghost" href="practice-areas.html">Practice Areas</a>
      <a class="btn btn--ghost" href="contact.html">Contact Us</a>
    </div>
  </div>
</section>
""" + foot()


PAGES = {
  "index.html": page_home,
  "about.html": page_about,
  "practice-areas.html": page_areas,
  "team.html": page_team,
  "yunus-abdulsalam.html": page_principal,
  "publications.html": page_pubs,
  "contact.html": page_contact,
  "404.html": page_404,
}

def write_seo_files():
    import datetime
    today = datetime.date.today().isoformat()
    urls = "".join(
        f"""  <url>
    <loc>{SITE_URL}/{fn if fn != 'index.html' else ''}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{'1.0' if fn == 'index.html' else '0.8'}</priority>
  </url>
""" for fn in PAGES if fn != "404.html")
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>
""")
    with open(os.path.join(OUT, "site.webmanifest"), "w", encoding="utf-8") as f:
        f.write("""{
  "name": "Yunus Abdulsalam SAN & Co.",
  "short_name": "YAS Legal",
  "description": "Legal Practitioners & Arbitrators, Asokoro, Abuja.",
  "start_url": "/",
  "display": "browser",
  "background_color": "#ffffff",
  "theme_color": "#13315c",
  "icons": [
    { "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "/apple-touch-icon.png", "sizes": "180x180", "type": "image/png" }
  ]
}
""")
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"""User-agent: *
Allow: /
Disallow: /_source/

Sitemap: {SITE_URL}/sitemap.xml
""")
    print("wrote sitemap.xml, robots.txt")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, gen in PAGES.items():
        with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
            f.write(gen())
        print("wrote", fn)
    write_seo_files()
