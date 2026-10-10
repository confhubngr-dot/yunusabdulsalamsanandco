# -*- coding: utf-8 -*-
"""Content model for the Yunus Abdulsalam SAN & Co. website."""

FIRM   = "Yunus Abdulsalam SAN &amp; Co."
TAG    = "Legal Practitioners &amp; Arbitrators"
PHONE  = "+234 706 124 1532"
PHONE_HREF = "+2347061241532"
EMAIL  = "info@yaslegal.org"            # public address: header, footer, contact page, enquiry form
EMAIL_PARTNER = "yunusabdulsalam@yaslegal.org"   # Principal Partner's direct address (bio + team pages)
ADDR_L1 = "Flat D2, Hampton Apartment, No. 2 Mungo Park Close"
ADDR_L2 = "Off Jesse Jackson Street, Asokoro, Abuja, FCT, Nigeria"

# ---------------------------------------------------------------- practice areas
# (slug, title, [paragraphs], [ (bold, text) bullets ] )
AREAS = [
 ("debt-recovery", "Debt Recovery", [
  "Our flagship practice. We act swiftly to minimise exposure, recover assets, and restore value — combining litigation, interlocutory applications, enforcement proceedings, and negotiated settlements. Where necessary, we act as Receiver/Manager over debtor assets.",
  "Working with financial experts to assess debt portfolios and build cases that withstand judicial scrutiny, we have achieved substantial recoveries for commercial banks, financial institutions, and private clients — including AMCON."], []),

 ("energy-law", "Energy Law", [
  "Strategic counsel across the oil, gas, and power sectors: exploration and production agreements, joint ventures, power purchase agreements, licensing, environmental compliance, and local content regulations.",
  "We represent energy companies, investors, regulators, and service providers in negotiations, regulatory engagements, and disputes — including cross-border transactions."], []),

 ("tax-litigation", "Tax Litigation", [
  "We represent clients at every stage of tax proceedings — contesting assessments and levies, and defending enforcement actions — before Tax Appeal Tribunals and courts across Nigeria.",
  "Whether through objections, appeals, or negotiated settlements, we challenge unlawful or excessive tax liabilities with a focus on efficiency and results."], []),

 ("shipping-maritime", "Shipping and Maritime", [
  "Comprehensive representation for importers, exporters, ship owners, charterers, dock operators, and logistics companies.",
  "Our experience spans admiralty litigation and arbitration — vessel arrests, charterparty disputes, cargo claims, marine insurance, and enforcement of maritime judgments — plus regulatory and financing advice for the industry."], []),

 ("property-law", "Real and Personal Property Law", [
  "We represent clients in the full range of property disputes: ownership and title conflicts, boundary issues, landlord and tenant matters, and recovery of premises.",
  "Beyond disputes, we handle title perfection, conveyancing, mortgages, leases, and property development transactions for individuals, corporates, and housing schemes."], []),

 ("oil-and-gas", "Oil and Gas Law", [
  "Specialised advisory and representation across the entire value chain — exploration and production, joint ventures, licensing, regulatory compliance, and environmental disputes.",
  "We guide operators, service companies, investors, and regulators through Nigeria's oil and gas framework, and handle contractual disputes and cross-border arbitration within the sector."], []),

 ("administrative-law", "Administrative Law", [
  "When public authorities act beyond their powers or in violation of due process, we respond with certiorari, mandamus, and prohibition.",
  "We also represent clients in regulatory disputes, licensing issues, compliance challenges, and enforcement actions — protecting business continuity throughout."], []),

 ("arbitration", "Arbitration", [
  "Robust representation in domestic and international arbitration across oil and gas, construction, corporate transactions, intellectual property, and financial services.",
  "We appear before arbitral tribunals and mediation panels, and before Nigeria's superior courts on the enforcement or challenge of arbitral awards — including cross-border and high-value commercial claims."], []),

 ("litigation", "Litigation and Civil Procedure", [
  "Litigation is at the heart of our practice. We prosecute and defend civil and commercial disputes, debt recovery, property claims, corporate litigation, election petitions, and regulatory challenges — from trial courts to the appellate level.",
  "Our command of procedural rules and courtroom strategy extends to enforcement proceedings, appeals, and urgent applications in complex, high-stakes cases."], []),

 ("labour-employment", "Labour and Employment", [
  "We advise employers, employees, and labour organisations across industries on workplace matters:"], [
  ("Regulatory compliance", "labour standards, workplace safety, and anti-discrimination laws."),
  ("Contracts &amp; policies", "employment agreements, confidentiality and non-compete clauses, and employee handbooks."),
  ("Union &amp; labour disputes", "collective bargaining, industrial actions, and disputes with labour organisations."),
  ("Workforce restructuring", "layoffs, redundancies, and outsourcing balanced against employee rights."),
  ("Dispute resolution", "wrongful termination, wage, and discrimination claims — through mediation, arbitration, and litigation.")]),

 ("assets-recovery", "Assets Recovery", [
  "We move quickly to prevent the dissipation of assets — deploying Mareva injunctions, Anton Piller orders, interim injunctions, and garnishee proceedings — and to trace and restore assets already concealed or transferred.",
  "We act for individuals, corporates, and institutions in matters of fraud, financial misconduct, breach of trust, and corporate malfeasance."], []),

 ("chieftaincy", "Chieftaincy Matters", [
  "We blend modern legal expertise with deep respect for tradition in disputes over traditional titles and succession.",
  "Our team litigates challenges to ascensions, coronations, succession rights, restraining injunctions, and recognition of traditional rulers — with sensitivity to cultural and community dynamics."], []),

 ("intellectual-property", "Intellectual Property", [
  "We protect, manage, and enforce intellectual assets across industries:"], [
  ("Patents &amp; trademarks", "registration, portfolio management, and defence of brand identities and innovations."),
  ("Copyrights", "protecting literary, artistic, digital, and software works from unauthorised use."),
  ("Trade secrets", "policies and agreements that safeguard sensitive business data."),
  ("IP litigation", "infringement disputes at home and across international jurisdictions."),
  ("Licensing", "technology-transfer agreements that maximise the commercial value of IP.")]),

 ("fundamental-rights", "Fundamental Rights", [
  "Driven by the belief that every individual is entitled to dignity, fairness, and protection under the Constitution, we pursue enforcement actions, interlocutory reliefs, and appellate advocacy.",
  "Our cases span unlawful detention, denial of due process, violations of freedom of expression and association, and discrimination — in both fee-paying and pro bono engagements."], []),

 ("consultancy-advisory", "Consultancy and Advisory Services", [
  "Practical, forward-looking counsel on mergers and acquisitions, joint ventures, corporate restructuring, and strategic investments — structured to minimise risk and align with long-term objectives.",
  "Beyond transactions, we provide ongoing advice on regulatory compliance, governance, dispute prevention, and risk management."], []),

 ("corporate-commercial", "Corporate &amp; Commercial", [
  "Full-service support for businesses at every stage of growth — from established corporations and financial institutions to SMEs and startups.",
  "Our expertise spans M&amp;A, joint ventures, corporate restructuring, governance, and the negotiation and drafting of commercial contracts — legal precision with commercial insight."], []),

 ("family-law", "Family Law", [
  "Trusted, discreet guidance on wills and testamentary dispositions, inter vivos property arrangements, and estate administration for executors and beneficiaries.",
  "We also represent clients in matrimonial causes, custody matters, and post-marital negotiations — with respect, fairness, and care."], []),

 ("election-petition", "Election Petition", [
  "We represent petitioners and respondents in highly contested electoral disputes — gubernatorial, legislative, and local government — before tribunals, appellate courts, and the Supreme Court.",
  "Experience with the technical and procedural demands of election litigation lets us manage high-stakes disputes with precision and discretion."], []),

 ("corporate-litigation", "Corporate Litigation", [
  "Strong representation in shareholder conflicts, boardroom disagreements, executive employment issues, and governance disputes that shape the direction and stability of companies.",
  "Through litigation, arbitration, or negotiated settlement, we resolve disputes efficiently while minimising business disruption."], []),

 ("criminal-law", "Criminal Law", [
  "Skilled representation in both defence and prosecution — from police investigations and bail applications to full trial advocacy and appeals.",
  "We scrutinise evidence, challenge procedural irregularities, and protect the rights of the accused. Our pro bono work has secured acquittals, reduced sentences, and corrected wrongful convictions."], []),

 ("tort-personal-injury", "Tort and Personal Injury", [
  "First-class representation in negligence, nuisance, trespass, occupiers' liability, and personal injury claims — for individuals, high-net-worth clients, and corporates.",
  "We also have strong expertise in defamation, both prosecuting and defending libel and slander cases where reputational integrity is on the line."], []),
]

# ---------------------------------------------------------------- values
VALUES = [
 ("Client Commitment", "Clients are at the heart of our practice. We design tailored strategies that protect their interests and give them clarity and confidence."),
 ("Distinction", "We stand out through the quality of our work and the impact of our advocacy — consistently raising the bar in our profession."),
 ("Ethical Leadership", "We lead with principle: honesty, transparency, and fairness shape every engagement."),
 ("Collaboration", "Great outcomes are collective. Teamwork and shared knowledge give every client the full strength of the firm."),
 ("Innovation &amp; Growth", "We embrace change and continuous learning to provide forward-looking legal solutions."),
 ("Service to Society", "Law is service beyond self. Through community initiatives and justice-oriented work, we help build a fairer society."),
]

# ---------------------------------------------------------------- team
# (name, role, photo|None, link|None)
TEAM = [
 ("Olufemi J. Mese",        "Associate", "olufemi-mese.jpg", None),
 ("Abdulwasiu M. Olatunji", "Associate", "abdulwasiu-olatunji.jpg", None),
 ("David Okeke",            "Associate", "david-okeke.jpg", None),
 ("Fatihu Abdulraheem",     "Associate", "fatihu-abdulraheem.jpg", None),
 ("Muhammed A. Omopupa",    "Associate", "muhammed-omopupa.jpg", None),
 ("Ahmad Abdulwahab",       "Associate", "ahmad-abdulwahab.jpg", None),
 ("Habeeb O. Lawal",        "Associate", "habeeb-lawal.jpg", None),
 ("Akande Mercy Oremeyi",   "Head of Human Resources", "akande-mercy.jpg", None),
 ("Fatima Binta Shehu",     "Associate", "fatima-shehu.jpg", None),
]

# ---------------------------------------------------------------- icons
# 24x24 stroke icons (drawn with currentColor)
ICONS = {
 "debt-recovery":        '<rect x="2.5" y="6" width="19" height="12.5" rx="2"/><circle cx="12" cy="12.2" r="2.6"/><path d="M6 9.5h.01M18 15h.01"/>',
 "energy-law":           '<path d="M13 2.5 5 14h6l-1.5 7.5L18 10h-6z"/>',
 "tax-litigation":       '<circle cx="12" cy="12" r="9.5"/><path d="M8.2 15.8 15.8 8.2"/><circle cx="9" cy="9" r="1.3"/><circle cx="15" cy="15" r="1.3"/>',
 "shipping-maritime":    '<circle cx="12" cy="5.5" r="2.4"/><path d="M12 8v13"/><path d="M5 13a7 7.5 0 0 0 14 0"/><path d="M8.5 13H5M19 13h-3.5"/>',
 "property-law":         '<path d="M3 11.5 12 3.5l9 8"/><path d="M5.5 10v10.5h13V10"/><path d="M10 20.5v-5h4v5"/>',
 "oil-and-gas":          '<path d="M12 3s6.3 7.3 6.3 11.2a6.3 6.3 0 0 1-12.6 0C5.7 10.3 12 3 12 3z"/>',
 "administrative-law":   '<path d="M3.5 9.5 12 3.5l8.5 6"/><path d="M6 10v7.5M10 10v7.5M14 10v7.5M18 10v7.5"/><path d="M3.5 21h17M3.5 17.5h17"/>',
 "arbitration":          '<path d="M12 3.5v17M8.5 20.5h7M4.5 6.5h15"/><path d="M6.5 6.5 4 12.3a2.9 2.9 0 0 0 5.8 0L7.3 6.5M17.5 6.5l-2.5 5.8a2.9 2.9 0 0 0 5.8 0l-2.5-5.8"/>',
 "litigation":           '<path d="m13.5 4.5 6 6"/><path d="m10 8 6 6"/><path d="m12 6 5.5 5.5"/><path d="M3 21l7.5-7.5"/><path d="M13.5 21H21"/>',
 "labour-employment":    '<circle cx="9" cy="8" r="3.4"/><path d="M2.8 20a6.3 6.3 0 0 1 12.4 0"/><path d="M15.7 5.2a3.4 3.4 0 0 1 0 6.3"/><path d="M17.6 14.4a6.3 6.3 0 0 1 3.7 5.6"/>',
 "assets-recovery":      '<circle cx="10.5" cy="10.5" r="6.8"/><path d="m15.6 15.6 5.4 5.4"/><path d="M8 10.5h5M10.5 8v5"/>',
 "chieftaincy":          '<path d="m3.5 16.5 1.4-9 4.6 4 2.5-6 2.5 6 4.6-4 1.4 9z"/><path d="M5 20h14"/>',
 "intellectual-property":'<path d="M9.2 17.8a6.8 6.8 0 1 1 5.6 0l-.3 2.2H9.5z"/><path d="M10 22.5h4"/>',
 "fundamental-rights":   '<path d="m12 2.5 8 3.4v5c0 4.9-3.4 9.2-8 10.7-4.6-1.5-8-5.8-8-10.7v-5z"/><path d="m8.7 11.7 2.3 2.3 4.3-4.3"/>',
 "consultancy-advisory": '<circle cx="12" cy="12" r="9.5"/><path d="m15.7 8.3-2.3 5.1-5.1 2.3 2.3-5.1z"/>',
 "corporate-commercial": '<rect x="5" y="3" width="14" height="18"/><path d="M9 7h2m2 0h2M9 11h2m2 0h2M9 15h2m2 0h2"/><path d="M10.5 21v-3h3v3"/>',
 "family-law":           '<path d="M12 20.5S3.8 15.4 2.6 10.7A5.1 5.1 0 0 1 12 6.6a5.1 5.1 0 0 1 9.4 4.1C20.2 15.4 12 20.5 12 20.5z"/>',
 "election-petition":    '<rect x="4" y="10" width="16" height="10" rx="1.5"/><path d="m8 10 1.5-5h5L16 10"/><path d="m9.8 14 1.8 1.8 3.2-3.2"/>',
 "corporate-litigation": '<rect x="3" y="8" width="18" height="12" rx="2"/><path d="M9 8V5.7A1.7 1.7 0 0 1 10.7 4h2.6A1.7 1.7 0 0 1 15 5.7V8"/><path d="M3 13.5h18"/>',
 "criminal-law":         '<rect x="4.5" y="3" width="15" height="18" rx="1.5"/><path d="M8.5 3v18M12 3v18M15.5 3v18"/>',
 "tort-personal-injury": '<rect x="3" y="6.5" width="18" height="14" rx="2"/><path d="M12 10.5v6M9 13.5h6"/><path d="M9 6.5V5a1.5 1.5 0 0 1 1.5-1.5h3A1.5 1.5 0 0 1 15 5v1.5"/>',
}

VALUE_ICONS = [
 '<circle cx="12" cy="8" r="3.6"/><path d="M4.5 20.5a7.5 7.5 0 0 1 15 0"/><path d="m14.5 8.5 2 2 3.5-3.5"/>',
 '<circle cx="12" cy="9" r="5.3"/><path d="M9.2 13.6 7.5 21l4.5-2.4L16.5 21l-1.7-7.4"/>',
 '<path d="M12 3.5v17M8.5 20.5h7M4.5 6.5h15"/><path d="M6.5 6.5 4 12.3a2.9 2.9 0 0 0 5.8 0L7.3 6.5M17.5 6.5l-2.5 5.8a2.9 2.9 0 0 0 5.8 0l-2.5-5.8"/>',
 '<circle cx="9" cy="8" r="3.4"/><path d="M2.8 20a6.3 6.3 0 0 1 12.4 0"/><path d="M15.7 5.2a3.4 3.4 0 0 1 0 6.3"/><path d="M17.6 14.4a6.3 6.3 0 0 1 3.7 5.6"/>',
 '<path d="M9.2 17.8a6.8 6.8 0 1 1 5.6 0l-.3 2.2H9.5z"/><path d="M10 22.5h4"/>',
 '<circle cx="12" cy="12" r="9.5"/><path d="M2.5 12h19"/><path d="M12 2.5c3.2 3.2 3.2 15.8 0 19-3.2-3.2-3.2-15.8 0-19z"/>',
]

# ---------------------------------------------------------------- publications
# HOW TO ADD A PUBLICATION
# Add one line to the relevant list below, then run:  python3 _source/build.py
# Format: (year, "Title", "Publisher / outlet", "https://link", "One-line description.")
# Newest first. Use "" for the link if none exists.

PUBS_ARTICLES = [
 ("2021", "Pantami in the Eyes of the Law", "PRNigeria",
  "https://prnigeria.com/2021/05/12/pantami-eye-law/",
  "A legal analysis of the controversy around Minister Isa Pantami, examining the boundary between legality and morality in public office."),
 ("2015", "Dasuki&rsquo;s Travails and the Rule of Law", "Daily Post Nigeria",
  "https://dailypost.ng/2015/11/08/yunus-abdulsalam-dasukis-travails-and-the-rule-of-law/",
  "On the detention of a former National Security Adviser and why government must respect court orders and due process."),
 ("", "Implementation of the Pension Reform Act", "Seminar paper &middot; Y.W.C. Publishers",
  "",
  "Conference paper presented at a seminar on the implementation of Nigeria&rsquo;s Pension Reform Act."),
]

PUBS_NEWS = [
 ("2026", "PRNigeria Founder Heads to Appeal Court over &#8358;1bn Suit Against NIPSS", "PRNigeria",
  "https://prnigeria.com/2026/06/29/prnigeria-founder-heads-appeal/",
  "The firm, led by Yunus Abdulsalam SAN, takes a fundamental-rights dispute to the Court of Appeal."),
 ("2026", "Court to Deliver Judgement in PRNigeria Founder&rsquo;s &#8358;1bn Suit", "Daily Post Nigeria",
  "https://dailypost.ng/2026/06/28/court-to-deliver-judgement-in-prnigeria-founders-n1bn-suit-against-nipss-june-29/",
  "Coverage of the firm&rsquo;s high-profile suit before the Federal High Court, Abuja."),
 ("2024", "Ex-NSA Dasuki Makes Rare Appearance as 38-Year-Old Yunus Abdulsalam Becomes SAN", "The Nation",
  "https://thenationonlineng.net/ex-nsa-dasuki-makes-rare-appearance-as-38-year-old-yunus-abdulsalam-becomes-san/",
  "The Principal Partner&rsquo;s conferment as one of Nigeria&rsquo;s youngest Senior Advocates."),
]
