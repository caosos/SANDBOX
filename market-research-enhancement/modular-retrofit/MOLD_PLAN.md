# Mold and Prototype Plan

## Principle

Do not start by modifying an expensive doll.

Start with molds, material samples, and test blocks. Prove the collar/socket, insert retention, cleaning, and tear resistance before touching a real product.

## Mold Path 1: Rigid 3D-Printed Mold

Best for the first working prototype.

Steps:

1. Design insert and collar geometry in CAD.
2. Print a two-piece rigid mold using SLA resin or sealed FDM.
3. Add registration keys so the halves align.
4. Add pour channel and air vents.
5. Sand and polish the cavity surface.
6. Apply compatible mold release.
7. Cast selected silicone or soft material.
8. Cure fully.
9. Demold.
10. Trim flash and inspect.
11. Test fit in sample socket.

Advantages:

- fast
- cheap
- repeatable
- easy to revise
- good for learning geometry

Risks:

- resin can inhibit platinum silicone cure if not fully cleaned/cured
- FDM layer lines may show in the part
- mold may wear out or crack
- release system matters

## Mold Path 2: Hand-Made Master + Mold Box

Best for cheap shape exploration.

Steps:

1. Shape a master from clay, wax, or printed plastic.
2. Smooth and seal the surface.
3. Build a mold box.
4. Embed half the master.
5. Pour first mold half.
6. Add registration keys.
7. Apply release.
8. Pour second mold half.
9. Remove master.
10. Cast test parts.

Advantages:

- cheap
- does not require perfect CAD at first
- good for learning size and feel

Risks:

- less repeatable
- harder to control wall thickness
- harder to standardize later

## Mold Path 3: Production Tooling

Only after the geometry, material, and collar design are proven.

Options:

- machined plastic molds
- aluminum molds
- outsourced silicone injection tooling
- multi-cavity molds

Do not spend serious tooling money before proving demand and mechanical survival.

## Important Silicone Mold Warning

Casting silicone inside a silicone mold can bond to itself unless the correct release system and compatible materials are used.

For early prototypes, rigid molds are usually easier than silicone-on-silicone casting.

## Bench Test Blocks

Create separate test blocks for TPE-like and silicone-like materials.

Test block features:

- simulated wall thickness
- rounded cut opening
- unreinforced control opening
- reinforced collar opening
- repeatable insert socket

Test:

- tear propagation
- pull-out force
- insert retention
- repeated install/removal cycles
- adhesive compatibility
- cleaning/drying access
- heat exposure
- lubricant/cleaner compatibility
- long-term softness or swelling

## Collar Geometry Tests

Test at least five collar approaches:

1. Adhesive-only flexible rim
2. Flanged collar bonded from the outside
3. Two-piece compression collar
4. Mesh-reinforced bonded collar
5. Mechanical-lock collar with flexible lip

Measure:

- installation difficulty
- tear resistance
- insert retention
- cleanup time
- failure mode

## Insert Geometry Tests

Start simple.

Core geometry:

- tapered body
- rounded rear flange
- removal tab or grip flange
- smooth exterior
- keyed alignment feature if needed
- drain/dry access path if compatible with design

Avoid early complexity:

- no internal battery
- no Bluetooth
- no app
- no heat until mechanical system works
- no complicated electronics until passive insert survives testing

## 5V Powered Prototype Path

After passive testing, add optional low-voltage features.

Architecture:

- UL-listed 5V wall adapter
- external control box
- inline fuse or current limiting
- PWM motor control if vibration is tested
- waterproof connector
- silicone-insulated wire
- strain relief
- removable powered insert

Rules:

- keep all power low-voltage DC
- disconnect before cleaning
- no mains voltage in product
- no sealed lithium battery in early version
- no heat without sensor and cutoff

## First Physical Prototype Sequence

1. CAD sketch of collar and insert.
2. Print small collar test rings first.
3. Cast sample collars.
4. Cut openings into test blocks.
5. Install collars.
6. Pull-test collars.
7. Cast passive inserts.
8. Test repeated insertion/removal.
9. Run cleaning/drying tests.
10. Revise geometry.
11. Move to sacrificial torso/damaged doll only after test blocks survive.

## Pass/Fail Criteria

A prototype fails if:

- cut edge tears after repeated cycles
- collar peels away
- insert pulls out too easily
- moisture is trapped behind the collar
- cleaning requires unrealistic effort
- material swells, gets sticky, or degrades
- powered version heats unpredictably
- cable strain relief fails

A prototype passes only if:

- collar survives repeated stress
- insert is removable without damage
- cleaning/drying is practical
- install process is repeatable
- failure mode is visible and not hidden
- the system can be explained simply to a customer

## Core Engineering Statement

The mold makes the part.

The collar makes the business.
