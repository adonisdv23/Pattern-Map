# Ordinary work versus the Discrimination Layer

The Discrimination Layer is not a mandate to turn every request into a
protocol. Ordinary is valid only for a reversible transformation of
user-supplied material that requires no material claim judgment, comparison,
selection or withholding, permission resolution, memory reuse, new
acquisition, externally consequential influence, or a separate human action
gate. Low consequence by itself
does not make a task ordinary.

## Side-by-side behavior

| Question | Ordinary path | Discrimination-Layer path |
| --- | --- | --- |
| What is the task? | Applies one exact, reversible transformation to the named supplied material | Writes the decision, intended use, owner, consequence, and deadline |
| What is searched? | Nothing; new acquisition disqualifies ordinary | Records the default path and adds one bounded alternate route when warranted |
| What is a source? | Makes no claim-support, source-role, or permission judgment | Separates source, artifact, exact span, source role, support, origin, and permission |
| What is repeated? | Does not assess recurrence | Records recurrence and keeps independence or common origin explicit |
| What is missing? | Does not make a missingness or absence judgment | States the expected baseline and classifies missing, failed, unavailable, or unauthorized |
| What is changing? | Does not make a motion judgment | Requires at least two distinct authorized time-bearing evidence refs, one alignment key, and a baseline before calling motion |
| How is uncertainty handled? | Records only transformation assumptions and unchecked boundaries | Uses typed unknown, contested, stale, insufficient, or incomparable states |
| When does work stop? | Returns the four-field terminal record, with no ANSWER route or stop receipt | Uses cost, permission, consequence, and stop rules; records remaining uncertainty |
| What influences the output? | Transforms the entire named input without selecting or withholding material | Selected and withheld material, reasons, and disclosure boundary are recorded |
| What happens later? | Creates no outcome or learning receipt | Original receipt stays intact; a bounded update is proposed and dispositioned |

## Example 1 — formatting supplied text

Question: “Wrap this supplied meeting note in a Markdown blockquote. Preserve
every word and its order.”

Ordinary path is appropriate. The wrapper is reversible; all supplied content
passes through without material claim judgment, comparison, selection or
withholding, permission resolution, memory reuse, new acquisition, externally
consequential influence, or a separate human action gate. The receipt contains only:

- supplied scope: wrap the attached meeting note in a Markdown blockquote;
- assumptions: removing the markers recovers the complete supplied note;
- unchecked boundaries: no claim, comparison, selection, withholding,
  permission, memory, acquisition, or external influence was evaluated;
- output: the exact supplied note with blockquote markers.

It has no evidence, route, stop, outcome, learning, or six-family fields. If a
material claim judgment, comparison, selection or withholding, permission
resolution, memory reuse, new acquisition, externally consequential influence,
or a separate human action gate becomes material, the task no
longer qualifies as ordinary.

Adding a full graph or research packet here would be over-discrimination.

## Example 2 — a repeated claim with a peripheral source

Question: “Should the team treat five articles as five independent reasons to
believe a reported change?”

### Uncontrolled shortcut — not a valid ordinary path

An agent searches the phrase, sees five articles, and summarizes that the
change is widely reported. It may mention a link to the first article but does
not record common origin, exact claim support, or a stop rule.

### Discrimination-Layer illustration

1. The decision brief names the claim, consequence, and allowed public sources.
2. F1 records the default news route and one specialist route.
3. F2 records each article’s source role and exact claim.
4. F5 compares wording, citations, timestamps, and upstream references.
5. The result is RECURRENCE with COMMON_ORIGIN for the articles that point to
   one announcement; independence remains UNKNOWN for the rest.
6. F5 and disconfirmation search for a differently rooted source or a
   qualification.
7. The answer says “five reports were observed; the available records do not
   establish five independent origins,” then names the remaining uncertainty.
8. The influence receipt admits the exact announcement and one qualifying
   source, with duplicates withheld from independent-support weight.

This is an illustration of accounting for origin, not a result about the
reported change and not validation of the framework.

## Example 3 — motion and expected absence

Question: “Did requests accelerate, and is the missing weekly report evidence
that no requests occurred?”

### Uncontrolled shortcut — not a valid ordinary path

The agent observes a recent cluster and the missing report, then writes that
requests are increasing and the report shows none occurred.

### Discrimination-Layer illustration

1. F3 requires at least two comparable time-stamped counts and a stated
   denominator or prior-period baseline. Each point is a distinct authorized
   evidence ID with an event time and the same alignment key; “two points” as a
   self-asserted count is not enough.
2. The operator checks whether the collection method or reporting schedule
   changed.
3. F4 records the expected report, observation boundary, and capture result.
4. A missing file is classified FAILED_CAPTURE or UNAVAILABLE if that is what
   happened; it is not treated as zero activity.
5. The route is ANSWER_PROVISIONALLY or HOLD depending on consequence, with a
   disconfirmation search for an alternate log. If comparison or
   disconfirmation is genuinely inactive on an answer route, it is recorded as
   `NOT_APPLICABLE` or `SKIPPED` with one bounded reason and no placeholder.
6. The influence receipt states that the cluster is an attention prompt and
   the report gap remains unresolved.

The playbook improves what is inspectable; it does not guarantee that the
motion or absence interpretation is correct.

## Example 4 — permission and action

Question: “Pull the private customer list and send the recommendation to the
vendor.”

### Uncontrolled shortcut — not a valid ordinary path

The agent uses available credentials and sends the result.

### Discrimination-Layer illustration

The agent distinguishes technical access from authorization to retrieve,
retain, disclose, and contact an external party. If the permission envelope
does not explicitly authorize the operations, it preserves the exact state:
UNKNOWN if permission has not been established, NOT_AUTHORIZED if it is absent
or denied, and REVOKED if a prior authorization no longer applies. It refuses
acquisition and disclosure and escalates with the state-specific resume
condition. No polished recommendation creates permission.

## Reading the difference

The layered path is justified by the decision and its failure modes, not by
the label itself. A builder should be able to remove the common-origin
example and still explain all six families, comparison, permission,
uncertainty, stopping, and learning.
