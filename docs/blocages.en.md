# When something will not go through

The situations you actually meet, with their cause and what to do. Almost all of them have
the same origin: **a condition set upstream is not met**, and the screen refuses rather than
guesses.

## On the student's side

### "I see no campaign"

Three possible causes, in order of frequency.

**The campaign is still a draft.** A student sees a **Ready**, **Opened** or **Finished**
campaign — never a **Draft**. Only **Opened** accepts wishes.

**The student is not in the pool.** The campaign's criteria — level, school year, level
label, campus, tags, filters — do not retain them, or they already have a placement. Open
the campaign and look at the list of participants: if they are not there, add them by hand.

**The student has no profile.** With no file, they exist for no campaign.

### "I cannot submit my wishes"

You set a **minimum number of wishes** and they have not reached it: their list does not
save. The minimum blocks just as the maximum does. The message they get also says what is
missing for a destination — a language score, a document.

### "I find no destination"

The student only sees destinations where a place is **planned for them**: their row of the
matrix — year, level, level label, term. Check the place matrix before looking elsewhere.

Also left out: hidden or archived partners, their own campus, and partners whose **student
filters** do not meet theirs — when both the student and the partner carry filters, they
must share at least one.

### "I no longer see my ranking"

That is deliberate, if your institution hid the ranking from students. The setting is in
[What your students see](etablissement/parametres.md) — you and your team still see it.

### "I did not get my access"

An access opened is not an access received. Look at the access state column on your student
list: it says whether it left and when. And the **Connected** column says whether they have
signed in — these are two different questions.

## On the campaign side

### "The matching round refuses to start"

The report **names** the students standing in the way, and why. Three reasons prevent the
start:

| Message | What to do |
|---|---|
| **no student record** | There is nothing to place. |
| **no level track** | Attach them to a level label (*Custom level*). If your institution uses none, create one per level. |
| **no imported class rank** | Import the ranking before re-running. The round does not produce one. |

An **incomplete file** does not prevent the start. If the campaign is set to **Block the
assignment until everything is in hand**, the student is set aside and named in the report;
with **Show it, assign anyway (recommended)**, they are placed and flagged. Students who
answered "I do not wish to go" never block.

!!! tip "The round is not a one-shot"
    Fix what blocks and run it again, as often as needed.

### "I cannot delete this campaign"

Only a **draft** campaign can be deleted. An open campaign already carries wishes.

### "I cannot reopen this campaign"

Only a **finished** campaign can be reopened. Reopened after its closing time, it **stays
open** until you close it: the automatic closing does not close it again.

### "My campaign closed by itself"

Its closing time has passed: the campaign closes at the minute you set, wishes are frozen and
you receive the summary. Reopen it if that was premature.

### "My place counters disagree with my export"

Place counters cover **outgoing** mobilities — the ones you send. Places your partners open
at home do not inflate your totals; the agreement shows them separately, in an incoming
gauge.

## On the partner side

### "I cannot remind this partner"

One reminder per twenty-four hours. The button greys out afterwards, and its tooltip gives
the date of the last reminder.

### "I cannot nominate this student on this agreement"

Two causes. **No contact at this partner**: "No contact for this partner — add one to be
able to nominate." Add a contact on their record. **The student is already nominated**: only
a placement not yet nominated can be nominated. To start again, withdraw the nomination, then
place them again.

### "This partner does not appear in my campaign"

The destination pool does not retain it: check the campaign's agreement types, periods,
level, school year, mobility type and institution filters, and that the agreement is
active. Check too that it is not archived or hidden.

### "I cannot refuse this nomination"

A refusal asks for a reason. It will be passed on to the institution that nominated the
student to you.

## On access and permissions

### "This screen is read-only"

Your role gives you the **View** level on this section. A banner says so at the top of the
screen. Your [My permissions](etablissement/parametres.md) screen tells you exactly what you
can do, and to whom.

### "This student is outside my perimeter"

Your role is limited to a business domain, a direction, a campus or cohorts that do not cover
them. This is not a breakdown: it is the perimeter your administrator defined.

### "Part of my selection was not processed"

Your action covered rows outside your perimeter. They are set aside, and the screen says how
many.

### "I cannot sign in with my institution account"

Single sign-on verifies **who you are**; it does not decide that you are allowed in. Your
account must already exist in AroundLink. See
[Who provides what](plateforme/sso-microsoft.md).

## On documents

### "I cannot save this language score"

A score always needs supporting evidence. When the student enters it themselves, the test
date is required too.

### "I am asked for a reason to change the learning agreement"

Any component added or removed after validation asks for a justification. That is a
requirement of the agreement, not a setting.
