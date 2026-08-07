# Yunus Abdulsalam SAN & Co. — Website Guide

This folder is the complete website. To put it online, upload everything in it
(except this README if you prefer) to any web host — Netlify, Vercel, cPanel,
GitHub Pages, or your hosting provider's file manager.

---

## The pages

| File | Page |
|---|---|
| `index.html` | Home |
| `about.html` | The Firm — history, vision, mission, values |
| `practice-areas.html` | All 21 practice areas |
| `team.html` | The full team with photos |
| `yunus-abdulsalam.html` | The Principal Partner's detailed bio |
| `publications.html` | Articles by the Principal Partner + press coverage |
| `contact.html` | Address, phone, email, enquiry form |
| `sitemap.xml`, `robots.txt` | For Google (see "Getting on Google" below) |

**How updating works (the one idea to understand):** all the words, names, and
lists live in one file — `_source/data.py`. You edit that file with any text
editor (Notepad, TextEdit, VS Code), then run one command, and every page is
rebuilt for you:

```bash
python3 _source/build.py
```

You need Python installed (free, python.org — most computers already have it).
Run the command from inside this `site` folder. Then re-upload the changed
HTML files to your host. That's the whole workflow. The sections below just
show you *where* in `_source/data.py` to make each kind of change.

---

## 1. Updating team members

### Add or change a photo

1. Get a photo of the person — a head-and-shoulders shot works best, ideally
   square, at least 480×480 pixels, saved as `.jpg`.
2. Name the file after the person, in lowercase with hyphens:
   `firstname-lastname.jpg` (e.g. `mary-okafor.jpg`).
3. Drop it into the **`assets/img/team/`** folder. (Replacing an existing
   file with a better photo? Keep the same filename — you're done, no rebuild
   needed.)

### Add, remove, or rename a person

1. Open `_source/data.py` and find the `TEAM` list. It looks like this:

   ```python
   TEAM = [
    ("Olufemi J. Mese",        "Associate", "olufemi-mese.jpg", None),
    ("Abdulwasiu M. Olatunji", "Associate", "abdulwasiu-olatunji.jpg", None),
    ...
   ]
   ```

   Each line is one person: **("Name", "Job title", "photo-filename.jpg", None)**.
   The order of the lines is the order they appear on the site.

2. To **add** someone: copy any line, paste it where you want them to appear,
   and change the name, title, and photo filename (the file you put in
   `assets/img/team/` in the step above). If you don't have their photo yet,
   write `None` (no quotes) instead of a filename — the site will show their
   initials in a circle until you add one.

   ```python
    ("Mary N. Okafor", "Senior Associate", "mary-okafor.jpg", None),
    ("John Doe",       "Associate",        None,              None),
   ```

3. To **remove** someone: delete their line.
4. To **rename** or change a title: edit the text between the quotes.
5. Save the file, then rebuild:

   ```bash
   python3 _source/build.py
   ```

6. Re-upload `index.html` and `team.html` (plus any new photos) to your host.

Team members appear in two places automatically: the circular strip on the
home page and the full grid on the team page.

---

## 2. Updating publications

1. Open `_source/data.py` and find `PUBS_ARTICLES` (things written **by** the
   firm) and `PUBS_NEWS` (press **about** the firm).
2. Add one entry per publication, newest first:

   ```python
   ("2026", "Title of the Article", "Outlet Name",
    "https://link-to-the-article",
    "One-line description of what it covers."),
   ```

   Use `""` for the link if there isn't one — the title will show as plain
   text instead of a link.
3. Save, rebuild (`python3 _source/build.py`), re-upload `publications.html`.

---

## 3. Updating contact details

At the very top of `_source/data.py`:

```python
PHONE  = "+234 706 124 1532"
PHONE_HREF = "+2347061241532"     # same number, no spaces — used for tap-to-call
EMAIL  = "yunusabdulsalam7@gmail.com"
ADDR_L1 = "Flat D2, Hampton Apartment, No. 2 Mungo Park Close"
ADDR_L2 = "Off Jesse Jackson Street, Asokoro, Abuja, FCT, Nigeria"
```

Edit, save, rebuild, re-upload — the header, footer, and contact page all
update together.

---

## 4. Updating practice areas

Find the `AREAS` list in `_source/data.py`. Each area is:

```python
("slug-name", "Title", [
 "First paragraph.",
 "Second paragraph."], []),
```

Edit the paragraphs freely. To add a whole new area, copy an existing block,
give it a unique slug (lowercase-with-hyphens), and add a matching icon entry
in the `ICONS` dictionary at the bottom of the file (copy any existing line as
a starting point).

---

## 5. Getting on Google (SEO)

The site already ships with everything Google looks for:

- **`robots.txt`** — tells search engines they're welcome, and where the sitemap is.
- **`sitemap.xml`** — lists every page so Google can find them all.
- **Structured data (JSON-LD)** on every page — tells Google this is a legal
  practice in Asokoro, Abuja, its phone number, hours, practice areas, and who
  the Principal Partner is. This is what powers rich results and the
  knowledge panel.
- Unique titles, meta descriptions, canonical URLs, and social-sharing tags
  on every page.

**Three things you must do at launch:**

1. **Set the real domain.** Open `_source/build.py`, find the line near the top:

   ```python
   SITE_URL = "https://www.example.com"
   ```

   Change it to your actual domain (no trailing slash), rebuild, and upload
   everything again — this fixes the sitemap, canonical links, and structured
   data in one go.

2. **Verify with Google Search Console** (free): search-console.google.com →
   add your domain → follow the verification step your host offers → then
   under "Sitemaps", submit `https://your-domain/sitemap.xml`. Bing has the
   same thing at bing.com/webmasters.

3. **Create a Google Business Profile** (free): business.google.com → add the
   firm with the exact same name, address, and phone number as the website.
   For a local law firm, this does more for Abuja search results than
   anything else on this list.

Worth doing soon after: get listed in Nigerian legal directories, and ask any
outlet that covers the firm to link to the site — links from real sites are
the main way Google decides a new website matters.

---

## 6. Other finishing touches

- **Logo:** the header uses a recreated monogram. To use the real logo, replace
  the `LOGO_SVG` block in `_source/build.py`, or ask your developer to swap in
  the original file.
- **Enquiry form:** currently opens the visitor's own email app with the
  message pre-filled. For messages that land directly in the firm's inbox,
  create a free account at formspree.io and point the form at it (or ask your
  host about form handling).
- **Team photo quality:** the current headshots were recovered from a
  photographed page of the firm profile, so they're soft at large sizes.
  Replacing them with each person's original photo (same filenames, in
  `assets/img/team/`) instantly upgrades the whole site.
