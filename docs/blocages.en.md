# When something will not go through

The situations you actually meet, with their cause and what to do. Almost all of them have
the same origin: **a condition set upstream is not met**, and the screen refuses rather than
guesses.

## On the student's side

### "I see no campaign"

Three possible causes, in order of frequency.

**The campaign is not open.** Only the **Opened** state accepts wishes. A "Ready" campaign is
visible to you, not to your students.

**The student is not in the pool.** The campaign's criteria — level, track, campus, tags,
filters — do not retain them. Open the campaign and look at the list of participants: if they
are not there, add them by hand.

**The student has no profile.** With no file, they exist for no campaign.

### "I cannot submit my wishes"

You set a **minimum number of wishes** and they have not reached it. The minimum blocks just
as the maximum does.

### "I find no destination"

The campaign's destination pool is empty, or no place is set on the agreements it retains.
Check the place matrix before looking elsewhere: a destination with no place does not show.

Check the **period** too: a place always exists for a given period.

### "I no longer see my ranking"

That is deliberate, if your institution hid the ranking from students. The setting is in
[What your students see](etablissement/parametres.md) — you and your team still see it.

### "I did not get my access"

An access opened is not an access received. Look at the access state column on your student
list: it says whether it left and when. And the **Connected** column says whether they have
signed in — these are two different questions.

## On the campaign side

### "The matching round refuses to start"

This is the most frequent block, and it is always explained: the report **names** the students
standing in the way, and why.

| Message | What to do |
|---|---|
| The student has **no track** | Attach them to one. If your institution uses none, create one per level. |
| The student has **no ranking** | Import the ranking before re-running. The round does not produce one. |
| The student has **no profile** | There is nothing to place. |
| Their **file is incomplete** | Complete it, or set the campaign to "flag" rather than "block". |

!!! tip "The round is not a one-shot"
    Fix what blocks and run it again, as often as needed.

### "I cannot delete this campaign"

Only a **draft** campaign can be deleted. An open campaign already carries wishes.

### "I cannot reopen this campaign"

Only a **finished** campaign can be reopened. And if you reopen it without pushing its end
date back, it will close again the next morning.

### "My campaign closed by itself"

Its end date has passed. That is normal behaviour since September 2026: the morning after the
last day, the campaign closes, draft wishes become wishes and you receive the summary. Reopen
it and push the date back if that was premature.

### "My place counters disagree with my export"

Since September 2026, every place counter covers **outgoing** mobilities only — the ones you
send. Places your partners open at home no longer inflate your totals. If a figure surprises
you, it was most likely wrong before.

## On the partner side

### "I cannot remind this partner"

One reminder per twenty-four hours. The button greys out afterwards, and tells you when.

### "I cannot nominate this student on this agreement"

A nomination is already live on that agreement for them. Withdraw it first if you want to
start again.

### "This partner does not appear in my campaign"

The destination pool does not retain it: check the campaign's agreement types, periods and
institution filters. Check too that it is not archived or hidden.

### "I cannot refuse this nomination"

A refusal asks for a reason. It will be passed on to the institution that nominated the
student to you.

## On access and permissions

### "This screen is read-only"

Your role gives you the **View** level on this section. A banner says so at the top of the
screen. Your [My permissions](etablissement/parametres.md) screen tells you exactly what you
can do, and to whom.

### "This student is outside my perimeter"

Your role is limited to a direction, a campus or cohorts that do not cover them. This is not a
breakdown: it is the perimeter your administrator defined.

### "Part of my selection was not processed"

Your action covered rows outside your perimeter. They are set aside, and the screen tells you
which.

### "I cannot sign in with my institution account"

Single sign-on verifies **who you are**; it does not decide that you are allowed in. Your
account must already exist in AroundLink. See
[Who provides what](plateforme/sso-microsoft.md).

## On documents

### "I cannot save this language score"

A score always needs supporting evidence. The file and the date are required.

### "I am asked for a reason to change the learning agreement"

Any component added or removed after validation asks for a justification. That is a
requirement of the agreement, not a setting.
