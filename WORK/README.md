# WORK — Michael's Work Operations Lane

## Standing rule

From 2026-08-30 forward, work-related planning and generated artifacts should be organized here in `caosos/SANDBOX/WORK/` unless Michael explicitly says otherwise.

This lane is for Michael's facility/work administration and operational support. It is separate from CAOSCare product development, which remains in `caosos/CAOSCARE.COM`.

## Use this lane for

- daily priority plans
- work request triage
- UTO / unit-turn tracking
- vacant-unit planning
- bill / invoice / PO follow-up trackers
- housekeeping schedules and staffing plans
- maintenance task lists and room punch lists
- vendor follow-up lists
- administrative checklists
- email-derived task summaries
- aging / overdue work reports
- workload and time estimates
- SOPs and reusable work templates
- sanitized CSV/Markdown summaries derived from exports

## Triage model

When enough information is available, rank work using:

1. resident impact / immediate operational impact
2. safety or regulatory exposure
3. hard deadline / financial consequence
4. age of request
5. dependency — whether this task blocks other work
6. estimated effort / travel / materials
7. delegation opportunity
8. current blocker or outside-vendor dependency

Preferred output states:

- NOW
- TODAY
- SCHEDULE
- DELEGATE
- WAITING / BLOCKED
- DEFER
- COMPLETE

## Work item fields

Use these fields when practical:

- title / request
- room / area
- department
- date requested
- due date / due window
- requester / source (sanitized when needed)
- status
- priority
- blocker
- estimated time
- vendor / PO / invoice reference (sanitized if needed)
- notes
- last action
- next action

## Privacy boundary

`caosos/SANDBOX` is a public repository. Do not store raw company-confidential exports, resident-identifying information, personnel details, medical information, private email contents, account numbers, or other non-public operational data here.

For raw work exports, use them transiently for analysis when authorized, then save only a sanitized operational summary or reusable template to this repository.

## Separation rule

- Work/job operations -> `caosos/SANDBOX/WORK/`
- CAOSCare product architecture/code -> `caosos/CAOSCARE.COM`
- If a work workflow becomes a generalized CAOSCare product requirement, document the generalized requirement in CAOSCare without copying private facility data.
