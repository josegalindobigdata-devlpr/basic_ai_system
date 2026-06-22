# TOS SIMPLE — EXECUTION WORKFLOW GUIDE

VERSION: 1.0  
PURPOSE: Practical execution guide for operating TOS_SIMPLE in ChatGPT / Gemini

---

# 1. CORE PRINCIPLE

FLOW:

TRUTH → EVALUATION → POSITIONING → EXECUTION

Modules:

- TOS_MASTER (control)
- TOS_1_BPA (truth)
- TOS_2_OME (evaluation)
- TOS_3_CPE (positioning)
- TOS_4_IPE (execution)

---

# 2. DAILY OPERATING MODEL

## STEP 0 — LOAD CONTEXT

Always start with:

- TOS_MASTER
- CURRENT_STATE
- Active opportunity (if exists)

---

# 3. WORKFLOW BY SCENARIO

---

## SCENARIO A — INITIAL SETUP

### Goal:
Establish professional baseline

### Steps:

1. Run TOS_1_BPA
2. Validate profile truth
3. Update TOS_MASTER:

CURRENT_STATE: STATE 1 — PROFILE_VALIDATED

---

## SCENARIO B — NEW JOB OPPORTUNITY

### Goal:
Decide if opportunity is worth pursuing

### Steps:

1. Update TOS_MASTER:
   CURRENT_STATE: STATE 2

2. Run TOS_2_OME

3. Decision:

- GO → proceed to CPE
- CONDITIONAL → evaluate risk
- NO-GO → discard and return to STATE 2

---

## SCENARIO C — POSITIONING PREPARATION

### Goal:
Adapt CV and narrative

### Steps:

1. Ensure OME = GO
2. Update TOS_MASTER:
   CURRENT_STATE: STATE 3

3. Run TOS_3_CPE

4. If READY:
   CURRENT_STATE: STATE 4

---

## SCENARIO D — INTERVIEW PREPARATION

### Goal:
Prepare for interview execution

### Steps:

1. Ensure positioning READY
2. Update TOS_MASTER:
   CURRENT_STATE: STATE 5

3. Run TOS_4_IPE

4. Prepare:
- answers
- stories
- objections
- compensation

---

## SCENARIO E — OFFER / FINAL DECISION

### Goal:
Evaluate and close

### Steps:

1. Update STATE: STATE 6
2. Evaluate offer manually
3. Decide:
   - Accept → STATE 7
   - Reject → STATE 7
   - Continue → STATE 5

---

# 4. STATE MACHINE SUMMARY

STATE 0 → PROFILE  
STATE 1 → READY PROFILE  
STATE 2 → OPPORTUNITY  
STATE 3 → EVALUATED  
STATE 4 → POSITIONED  
STATE 5 → INTERVIEW  
STATE 6 → OFFER  
STATE 7 → CLOSED  

---

# 5. OPERATING RULES

- Never skip states
- Never position without evaluation
- Never interview without positioning
- Always update TOS_MASTER manually
- Always reuse BPA truth

---

# 6. QUICK USAGE TEMPLATE

Copy this before each prompt:

---

READ FIRST:
- TOS_MASTER
- CURRENT_STATE
- ACTIVE OBJECTIVE

TASK:
[Describe task]

CONTEXT:
[Paste relevant data]

---

# 7. MINIMUM VIABLE FLOW

If you want ultra-simple usage:

1. BPA once
2. OME for each opportunity
3. CPE only for GO
4. IPE only for interviews

---

# 8. FINAL PRINCIPLE

Discipline > Complexity

This system works if:
- you respect the state flow
- you maintain truth
- you avoid reactive decisions

---

