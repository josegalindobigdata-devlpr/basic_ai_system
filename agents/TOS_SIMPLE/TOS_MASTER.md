# TALENT OPERATING SYSTEM (TOS) — MASTER CONTROL FILE
MODULE: TOS_MASTER
VERSION: SIMPLE_1.0
TYPE: GOVERNANCE
SYSTEM VERSION: SIMPLE ARCHITECTURE
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



# 2. CORE OPERATING PRINCIPLE

TRUTH → EVALUATION → POSITIONING → EXECUTION

No downstream action may violate upstream truth.

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
4. Relevant module
5. Active blockers
6. Strategic objective



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
