# TALENT OPERATING SYSTEM (TOS) — MASTER CONTROL FILE
<!-- TOS_SIMPLE v2.0 — Reescritura anti-deslizamiento. Sustituye a v1.0. -->
MODULE: TOS_MASTER
VERSION: SIMPLE_2.0
TYPE: GOVERNANCE
SYSTEM VERSION: SIMPLE_2.0 (3-LAYER ARCHITECTURE)
ARCHITECTURE: MARKDOWN-FIRST / PROMPT-ORCHESTRATED
SYSTEM TYPE: PORTABLE STRATEGIC DECISION FRAMEWORK
PRIMARY DOMAIN: TALENT | CAREER | POSITIONING | INTERVIEW



# 1. SYSTEM PURPOSE

TOS_MASTER is the canonical control layer for the simplified Talent Operating System.

Its purpose is to provide:

- single source of truth,
- strategic continuity,
- state governance,
- execution sequencing,
- profile integrity,
- decision discipline,
- and prompt interoperability

across all TOS modules:

- TOS_1_BPA
- TOS_2_OME
- TOS_3_CPE
- TOS_4_IPE



# 1A. THREE-LAYER ARCHITECTURE & DATA AUTHORITY

TOS_SIMPLE operates on three layers with disjoint responsibilities:

## DATA LAYER (SSOT) — Canonical source of truth. Cited LITERALLY.
- FACTS_SHEET.md — invariable constants: names, headline figures, anchor-role
  titles, certifications, education, citation rules. Final word in validation.
- MASTER_CV_RAW.md — full career history, exact per-role metrics, documented
  chronological decisions (decimals for internal audit only).
- TARGET_POSITIONS_PROFILE.md — matrix of the 3 Anchor Roles (SDM, GOV, DLV):
  client pains, ATS keywords, positioning strategy.

## METHOD LAYER — Engines. Govern the HOW, never the WHAT. Contain no data.
- TOS_1_BPA (truth validation method — validates and points to the DATA LAYER;
  it is NOT the source of the datum)
- TOS_2_OME, TOS_3_CPE, TOS_4_IPE

## GOVERNANCE LAYER — State, sequence, continuity.
- TOS_MASTER, TOS_SHARED_CONTEXT, CHANGELOG

## AUTHORITY HIERARCHY (precedence on any conflict, highest first)
1. DATA LAYER (FACTS_SHEET > MASTER_CV_RAW > TARGET_POSITIONS_PROFILE)
2. TOS_MASTER (state & sequence)
3. METHOD LAYER (BPA / OME / CPE / IPE)
4. TOS_SHARED_CONTEXT (continuity)

GOLDEN RULE: DATA prevails over METHOD. If an engine suggests anything that
contradicts a DATA LAYER file, the DATA wins. METHOD governs process and
structure, never figures, names or titles. If a required datum is absent from the
DATA LAYER, BLOCK — never invent or infer it.



# 2. CORE OPERATING PRINCIPLE

DATA (SSOT) → TRUTH → EVALUATION → POSITIONING → EXECUTION

No downstream action may violate upstream truth, and no truth, evaluation,
positioning or execution may override the DATA LAYER.

Mandatory sequence:

PROFILE → OPPORTUNITY → POSITIONING → INTERVIEW



# 3. SYSTEM IDENTITY

## PROFESSIONAL BASELINE
PROFILE_ID:
NAME:
TARGET ROLE:
PRIMARY INDUSTRY:
CORE EXPERIENCE:
YEARS OF EXPERIENCE:
KEY DOMAINS:
TOP CAPABILITIES:
LEADERSHIP LEVEL:
LANGUAGE STACK:
CERTIFICATIONS:
GEOGRAPHIC SCOPE:
COMPENSATION TARGET:
EMPLOYMENT PRIORITIES:



# 4. STRATEGIC OBJECTIVES

## PRIMARY OBJECTIVE
Example:
Secure senior PM / transformation / strategy role aligned with compensation and positioning targets.

## SECONDARY OBJECTIVES
- Compensation growth
- Strategic repositioning
- Industry shift
- Leadership expansion
- Certification leverage

## NON-NEGOTIABLES
- Minimum salary
- Remote / hybrid / onsite
- Sector restrictions
- Ethical constraints
- Geographic limits






# 5. CURRENT STATE MACHINE

## CANONICAL STATES

### STATE 0 — NO_PROFILE
No validated professional baseline.

### STATE 1 — PROFILE_VALIDATED
Professional truth established.

### STATE 2 — OPPORTUNITY_RECEIVED
New opportunity exists for evaluation.

### STATE 3 — OPPORTUNITY_EVALUATED
Opportunity scored for strategic fit.

### STATE 4 — POSITIONING_READY
Narrative, CV, and strategic positioning adapted.

### STATE 5 — INTERVIEW_ACTIVE
Interview execution in progress.

### STATE 6 — OFFER_DECISION
Offer under evaluation.

### STATE 7 — CLOSED_LOOP
Accepted / rejected / archived.

### STATE 8 — RECOVERY_REQUIRED
Critical inconsistency or governance drift detected.
Revalidation required before downstream execution.


# 6. CURRENT SYSTEM STATUS

CURRENT_STATE:
NEXT_ALLOWED_STATE:
ACTIVE_PRIORITY:
BLOCKERS:
CRITICAL_RISKS:
LAST_UPDATED:

# 6A. UNIVERSAL EXECUTION HEADER

Every module execution must begin with:

## SYSTEM VERSION:
## SESSION_ID:
## OPPORTUNITY_ID:
## CURRENT_STATE:
## ACTIVE_MODULE:
## ACTIVE_OPPORTUNITY:
## STRATEGIC_OBJECTIVE:
## LAST_BPA_VERSION:
## LAST_OME_DECISION:
## ACTIVE_RISKS:
## LAST_UPDATED:

This header is mandatory across:
- ChatGPT Projects
- Gemini Gems
- multi-chat workflows
- manual orchestration flows

Purpose:
- reduce context drift
- standardize state continuity
- improve prompt interoperability
- enforce operational traceability

# 7. STATE TRANSITION RULES

ALLOWED:

STATE 0 → STATE 1  
STATE 1 → STATE 2  
STATE 2 → STATE 3  
STATE 3 → STATE 4 OR STATE 2  
STATE 4 → STATE 5  
STATE 5 → STATE 6  
STATE 6 → STATE 7  
STATE 7 → STATE 2 OR STATE 0  

ANY STATE → STATE 8
STATE 8 → STATE 1 / 2 / 3 / 4

# 7A. STATE GOVERNANCE AUTHORITY

State transitions are manually governed.

The user is the final authority responsible for:

- CURRENT_STATE updates
- NEXT_ALLOWED_STATE updates
- LAST_UPDATED refresh
- blocker resolution tracking

Mandatory rule:

After every completed module execution:
- CURRENT_STATE must be reviewed
- transition validity must be verified
- blockers must be updated

No automatic transitions exist in TOS_SIMPLE.

# 8. EXECUTION BLOCKERS

Execution blocked if:

- No validated profile
- Opportunity not evaluated
- Positioning missing
- Narrative inconsistency
- Compensation misalignment
- Strategic mismatch
- State skipping



# 9. SHARED CANONICAL SCHEMAS

## PROFILE_MASTER
- Career history
- Role scope
- Leadership profile
- Delivery record
- Certifications
- Strategic differentiators
- Weaknesses
- Risk factors



## OPPORTUNITY_SCHEMA
- Company
- Role
- Compensation
- Strategic fit
- Capability match
- Risks
- Decision score



## POSITIONING_SCHEMA
- Tailored narrative
- CV adaptation
- Recruiter pitch
- Value proposition
- Objection handling



## INTERVIEW_SCHEMA
- Interview narrative
- STAR stories
- Executive positioning
- Compensation defense
- Risk mitigation

# 9A. STANDARD HANDOFF CONTRACT

All module transitions must include a standardized handoff package.

## REQUIRED HANDOFF STRUCTURE

### SOURCE MODULE:
### TARGET MODULE:
### SESSION_ID:
### OPPORTUNITY_ID:
### CURRENT_STATE:

## STRATEGIC CONTEXT
- active objective
- current opportunity
- strategic risks
- compensation boundaries
- positioning constraints

## REQUIRED INHERITED ASSETS
- latest PROFILE_MASTER
- latest opportunity evaluation
- latest risk register
- latest positioning strategy
- latest decision status

## VALIDATION STATUS
APPROVED / CONDITIONAL / BLOCKED

Purpose:
- reduce context fragmentation
- improve interoperability
- standardize module continuity
- preserve strategic coherence

# 10. DECISION FRAMEWORK

## DECISION AUTHORITY
Truth > Emotion

## GO / NO-GO LOGIC
GO if:
- Strategic fit
- Compensation fit
- Positioning viability
- Career leverage

NO-GO if:
- Misalignment
- Strategic regression
- Compensation dilution
- Brand damage



# 11. MEMORY SNAPSHOT

## ACTIVE OPPORTUNITIES
[Manual update]

## TOP PRIORITY TARGETS
[Manual update]

## CURRENT RISKS
[Manual update]

## STRATEGIC GAPS
[Manual update]

## RECENT OUTPUTS
[Manual update]



# 12. MODULE DIRECTORY

## DATA LAYER (SSOT) — Cited literally; final word in validation
### FACTS_SHEET.md
Purpose: invariable profile constants (names, headline figures, anchor titles,
certifications, education, citation rules).
Authority: highest. Overrides every method and narrative.

### MASTER_CV_RAW.md
Purpose: full career history and exact per-role metrics (internal audit).

### TARGET_POSITIONS_PROFILE.md
Purpose: matrix of the 3 Anchor Roles (SDM, GOV, DLV) — pains, ATS keywords,
positioning strategy.


## TOS_SHARED_CONTEXT
Purpose:
Operational continuity and shared context governance

Trigger:
Any state transition, opportunity update, positioning update, or execution refresh

Authority:
Context continuity only
Does not override:
- TOS_MASTER
- BPA truth
- OME evaluation
- CPE positioning
- IPE execution


## TOS_1_BPA
Purpose:
Professional truth and baseline governance

Trigger:
Profile creation or recalibration



## TOS_2_OME
Purpose:
Opportunity strategic analysis

Trigger:
New job / recruiter / internal role



## TOS_3_CPE
Purpose:
Strategic positioning adaptation

Trigger:
GO decision after evaluation



## TOS_4_IPE
Purpose:
Interview execution and conversion

Trigger:
Interview stage begins



# 13. REQUIRED UNIVERSAL PROMPT HEADER

Every module invocation must include:

READ ORDER:
1. TOS_MASTER
2. TOS_SHARED_CONTEXT
3. CURRENT_STATE
4. DATA LAYER (FACTS_SHEET / MASTER_CV_RAW / TARGET_POSITIONS_PROFILE)
5. Relevant method module (BPA / OME / CPE / IPE)
6. Active blockers
7. Strategic objective

Reminder: any datum produced must be traceable to the DATA LAYER. If method and
data disagree, the data wins (see §1A Golden Rule).



# 14. CHANGE CONTROL

VERSION:
LAST MAJOR UPDATE:
LAST STRATEGIC CHANGE:
CHANGE SUMMARY:



# 15. OPERATING RULES

RULE 1
Maintain profile truth.

RULE 2
Never position beyond validated truth.

RULE 3
No opportunity pursuit without evaluation.

RULE 4
No interview without positioning.

RULE 5
Protect long-term strategic value over short-term urgency.

RULE 6
Manual state updates required after every major transition.

RULE 7
DATA LAYER prevails over METHOD. Cite DATA LAYER values literally; never invent,
infer or round a profile datum that is absent. If method and data conflict, the
data wins.



# 16. SIMPLICITY ENFORCEMENT

This system is intentionally simplified.

No:
- autonomous memory,
- event bus,
- concurrency,
- hidden orchestration,
- automated rollback.

All governance is prompt-controlled and user-managed.



# 17. FINAL EXECUTIVE PRINCIPLE

TOS exists to maximize strategic career outcomes through disciplined sequencing.

TRUTH establishes credibility.  
EVALUATION protects direction.  
POSITIONING increases conversion.  
EXECUTION secures outcomes.



# OUTPUT DESIGNATION

TOS_MASTER  
MASTER CONTROL FILE  
SIMPLE ARCHITECTURE  
PRODUCTION VERSION  
