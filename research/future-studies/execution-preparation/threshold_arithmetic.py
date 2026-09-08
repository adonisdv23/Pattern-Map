"""Deterministic management-threshold arithmetic; no model or study data.

Reads no files, private rubrics, assignment records or environment values.
Run with Python's standard library; stdout is the companion arithmetic record.
"""
from fractions import Fraction


def ceil_fraction(value):
    return -(-value.numerator // value.denominator)


def main():
    tasks, surfaces, repeats, arms = 12, 2, 2, 3
    per_arm = tasks * surfaces * repeats
    slots = per_arm * arms
    print("AUTHORED THRESHOLD ARITHMETIC / NO OBSERVED OR SIMULATED PERFORMANCE")
    print(f"Base tasks: {tasks}; assignments per arm: {per_arm}; total: {slots}")
    print("delta_min | required net accepted assignments | realized threshold | largest eligible baseline count")
    for delta in (Fraction(1, 20), Fraction(1, 10), Fraction(3, 20)):
        gain = ceil_fraction(delta * per_arm)
        assert Fraction(gain - 1, per_arm) < delta <= Fraction(gain, per_arm)
        eligible = []
        for baseline in range(per_arm + 1):
            achievable = any(Fraction(proposed - baseline, per_arm) >= delta
                             for proposed in range(per_arm + 1))
            assert achievable == (baseline <= per_arm - gain)
            if achievable:
                eligible.append(baseline)
        print(f"{float(delta):.2f} | {gain} | {gain}/{per_arm} = {float(Fraction(gain, per_arm)):.6f} | {max(eligible)}")
    # An authored concentration example: five net successes can occupy two tasks.
    net = [4, 1] + [0] * 10
    overall = Fraction(sum(net), per_arm)
    loo = [Fraction(sum(net) - n, 4 * (tasks - 1)) for n in net]
    print(f"Concentration illustration, net task counts {net}: overall {overall}")
    print(f"Leave-one-task-out range: {min(loo)} to {max(loo)}; not a confidence interval")
    print("Proposed independent hard ceilings (not measured needs):")
    print(f"32,000 accounted tokens/episode: {per_arm * 32000:,}/arm; {slots * 32000:,} total")
    print(f"8 model requests/episode: {per_arm * 8}/arm; {slots * 8:,} total")
    print(f"180 seconds/episode: {per_arm * 180}/arm; {slots * 180:,} summed episode seconds = {slots * 180 / 3600:.1f} hours")
    print(f"2 acquisition units/episode: {per_arm * 2}/arm; {slots * 2} total")
    print(f"Proposed acquisition margin: +12 units/arm = {Fraction(12, per_arm)} unit per assigned episode; zero-extra is the stricter alternative")
    print(f"2 semantic reviews/episode: {slots * 2} initial reviews")
    print(f"1 separate action/procedure review/episode: {slots} adherence passes")
    minutes = 2 * 120 + slots * 2 * 3 + slots * 1 + 240 + 72
    assert minutes == 26 * 60
    print("Reviewer plan: 4h setup + 14.4h semantic reviews + 2.4h adherence passes + 4h adjudication + 1.2h reserve = 26 person-hours")
    price = Fraction(50 * 1000000, slots * 32000)
    print(f"USD50 / 4,608,000 tokens permits at most USD{float(price):.6f}/million at the maximum token price, if there are no other charges")
    print("Prices, tokenizer fit, actual elapsed enforcement and owner acceptance remain unverified.")


if __name__ == "__main__":
    main()
