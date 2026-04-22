# Severity And Review Dimensions

Use this reference when classifying findings and separating real defects from style preferences.

## Severity Rubric

### high

Use `high` when the issue can plausibly cause serious harm:

- Incorrect result, data corruption, data loss, or broken persistence.
- Security exposure such as injection, auth bypass, secret leakage, unsafe deserialization, or missing authorization.
- Production crash, resource leak, race condition, deadlock, or unbounded retry.
- Public API contract break, backward-incompatible schema change, or misleading status code that clients rely on.
- Financial, medical, safety, or compliance impact.

High-severity findings must be concrete. If the risk depends on unknown context, describe the condition instead of inflating severity.

### medium

Use `medium` when the issue is likely to create bugs or meaningful maintenance drag:

- Missing validation or incomplete error handling.
- Confusing state transitions.
- Strong coupling between unrelated responsibilities.
- Duplicate business logic that can diverge.
- Function/class doing too many things.
- Ambiguous type/data shape that makes callers guess.
- Poor testability around non-trivial behavior.

### low

Use `low` for local cleanup:

- Weak names that slow reading but do not mislead behavior.
- Small duplicated snippets.
- Slightly awkward control flow.
- Redundant comments.
- Minor inefficiency with no clear scale risk.

### nit

Use `nit` for tiny polish:

- Formatting inconsistency.
- Minor wording.
- Small import or ordering issue.

### preference

Use `preference` for subjective tradeoffs:

- `class` vs function style when both fit the codebase.
- Early returns vs a single exit when readability is debatable.
- Naming variants that are both clear.
- Framework-specific style when the repo has no convention.

Never call a preference a bug.

## True Issue Checklist

Before presenting a roast point as a real issue, check:

- Is there code evidence?
- Can the behavior fail, confuse maintainers, or increase change cost?
- Can the issue be explained without relying on personal taste?
- Is there a practical fix?
- Would another experienced engineer likely agree this is worth discussing?

If the answer is mostly "no", label it as a preference or omit it.

## Review Dimensions

### Readability

Look for dense expressions, unclear branching, deeply nested blocks, and mixed abstraction levels.

Useful fix patterns:

- Extract named helpers.
- Introduce guard clauses.
- Split transformation steps.
- Rename intermediates to reveal intent.

### Naming

Look for names that are too vague, misleading, overloaded, or inconsistent with domain language.

Useful fix patterns:

- Prefer domain-specific nouns and verbs.
- Rename boolean variables as predicates.
- Avoid `data`, `info`, `temp`, `manager`, or `handler` unless context makes them precise.

### Duplication

Look for repeated validation, mapping, API calls, error handling, and business rules.

Useful fix patterns:

- Extract shared helpers only when duplication has the same meaning.
- Avoid premature abstraction when repeated code is similar but not semantically identical.

### Function Responsibility

Look for functions that parse, validate, mutate state, call APIs, format output, and handle errors all at once.

Useful fix patterns:

- Split orchestration from pure logic.
- Keep side effects at boundaries.
- Give each helper one reason to change.

### Comments

Look for comments that restate code, disagree with code, explain a workaround without context, or hide unclear naming.

Useful fix patterns:

- Delete comments that restate obvious code.
- Replace misleading comments with clearer code.
- Keep comments that explain "why", constraints, and non-obvious tradeoffs.

### Error Handling

Look for swallowed errors, catch-all blocks, ambiguous fallback values, missing retries, missing logging, and exposed internal errors.

Useful fix patterns:

- Handle expected errors explicitly.
- Preserve original error context.
- Return typed/domain-specific errors where the codebase supports it.

### Boundary Conditions

Look for null/undefined/None, empty arrays, invalid IDs, duplicate inputs, time zones, precision, huge payloads, concurrency, and partial failures.

Useful fix patterns:

- Add input validation.
- Define empty-state behavior.
- Add tests for edge cases.

### Types And Data Structures

Look for `any`, untyped dictionaries/maps, implicit schemas, unclear optional fields, and multiple shapes using the same name.

Useful fix patterns:

- Use explicit types or schemas.
- Validate external data at boundaries.
- Keep internal invariants narrow.

### State Management

Look for shared mutable state, hidden mutation, stale closures, order-dependent updates, and confusing lifecycle ownership.

Useful fix patterns:

- Centralize state transitions.
- Make mutation explicit.
- Prefer immutable updates where the codebase expects them.

### API Contracts

Look for inconsistent response shapes, hidden breaking changes, unclear status codes, missing versioning, and undocumented optional fields.

Useful fix patterns:

- Align request/response types with implementation.
- Keep errors predictable.
- Document or test compatibility-sensitive behavior.

### Maintenance Cost

Look for code that makes future changes risky: tight coupling, unclear boundaries, fragile tests, config scattered across files, or duplicated domain rules.

Useful fix patterns:

- Reduce blast radius.
- Add characterization tests.
- Move domain rules to one owner.
