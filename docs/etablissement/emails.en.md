# Emails &amp; connectors

Exchanges with your partners live in your mail client, and the student's file lives in
AroundLink. **Filed emails** bring the two together: a message exchanged with a contact ends
up on their fiche, with nobody retyping anything.

!!! info "Where it happens"
    **Settings ▸ Connectors** brings the three connections together: **Email**, **Calendar**
    and **API**. Filed messages are then read on the fiches — partner, contact, student.

## Filing your emails without leaving Outlook

**What it is for.** Finding, six months later, what was said to a partner — without digging
through the mailbox of a colleague who is on holiday.

**Who it is for.** <span class="al-audience">the whole mobility team</span>

**How it works.** An **Outlook add-in** files the emails you exchange with your contacts on
the right fiche, from your mail client. A message is filed only when it is **authenticated**
and involves a **contact already in AroundLink**; everything else is read and forgotten.

Installation takes six steps, given directly on the page — Microsoft only allows an add-in to
be added from a buried page of its own site, and the second half of the guide (where to click
in Outlook once the add-in is in place) appears in no Microsoft documentation. Every delicate
step carries its screenshot.

1. download the add-in file — a single file, to keep until step 3;
2. open your Outlook add-ins, left column, **My add-ins**;
3. under **Custom add-ins**, **Add a custom add-in**, then **Add from file**;
4. open an email, then the **Apps** button in the message toolbar;
5. pick **AroundLink for Outlook** from the list;
6. pin the pane, so it stays open from one message to the next.

!!! tip "Without the add-in: the address in Cc"
    If the add-in is not an option, put your **institution's address** in Cc when you write to
    a contact: the message lands on their fiche. One button copies it from the Connectors
    page. It is a fallback, not the solution: you have to remember it on every message, which
    is the whole reason the add-in exists.

## Reading exchanges on a fiche

**What it is for.** Seeing the history of a relationship where you actually work.

**How it works.** Filed messages appear **identically on three screens**: a partner's fiche,
under **Relationship ▸ All emails** (the aggregate of its contacts' emails), a contact's
fiche, and a student's fiche, under **Emails**.

- **one card per message**, only one open at a time;
- the direction of the exchange is marked — received or sent;
- **names are links** when the person is on file with you; an unknown address stays plain
  text, which is the truth;
- attachments download from the card;
- **Reply** and **Forward** open your mail client with the message quoted.

On a student's fiche, emails are matched to their addresses — the school one and the personal
one. The list there is **read-only**: a message is managed from the fiche of the contact that
carries it.

In contact grids, a **Last contact** column gives the date of the latest exchange.

!!! warning "Nothing is deleted there"
    The email screens carry no destructive gesture. A message filed by mistake is handled on
    the administration side, not from a fiche — a relationship history that one click could
    empty would not be a history.

## The calendar and the API

**How it works.** The two other connections live in the same place.

- **Calendar** — read your AroundLink [agenda](agenda.md) from Outlook, Google Calendar or
  Apple Calendar. The link carries your whole agenda and reads **one way only**: your calendar
  comes to read, it changes nothing.
- **API** — let your own systems read and write AroundLink data. This connection is meant for
  your institution's IT team. **The key is personal, not your institution's**: everyone has
  their own, and regenerating it leaves a colleague's working.

**Use case.**
> The head of office writes to her counterpart in Bologna to settle the semester dates. The
> AroundLink pane is pinned in her Outlook: the message is filed on the contact's fiche. Three
> months later, her colleague opens the partner's fiche, reads the exchange, and replies from
> the card without searching her own mailbox.
