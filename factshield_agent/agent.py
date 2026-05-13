from google.adk.agents import Agent

def extract_core_claim(text: str) -> dict:
    cleaned = str(text).strip()
    return {"claim": cleaned}

def calculate_credibility_score(
    num_supporting: int,
    num_contradicting: int,
    has_authoritative_source: bool
) -> dict:
    score = 50
    score += (int(num_supporting) * 10)
    score -= (int(num_contradicting) * 15)
    if has_authoritative_source:
        score += 20
    score = max(0, min(100, score))
    if score >= 75:
        label = "LIKELY TRUE"
    elif score >= 50:
        label = "MISLEADING"
    elif score >= 25:
        label = "LIKELY FALSE"
    else:
        label = "FALSE"
    return {"score": score, "label": label}

root_agent = Agent(
    name="factshield_agent",
    model="gemini-2.5-flash",
    description="FactShield verifies claims using credibility scoring.",
    instruction="""
    You are FactShield - a precise, unbiased AI fact-checking agent.

    When given a claim:

    STEP 1: Call extract_core_claim() with the claim text.

    STEP 2: Use your knowledge to assess the claim against known facts
    from WHO, governments, peer-reviewed journals, BBC, Reuters.

    STEP 3: Call calculate_credibility_score() with:
    - num_supporting: number of sources that support the claim
    - num_contradicting: number of sources that contradict it
    - has_authoritative_source: true if WHO or govt or journal exists

    STEP 4: Reply with a nicely formatted response like this:

    ## 🔍 FactShield Verdict

    **Claim:** the claim here

    **Verdict:** ✅ TRUE / ❌ FALSE / ⚠️ MISLEADING / ❓ UNVERIFIED

    **Confidence:** 95%

    **Category:** Health / Science / Politics / Finance

    **Evidence:**
    - Source 1: what it says
    - Source 2: what it says

    **Reasoning:** Your 2-3 sentence explanation here.
    """,
    tools=[extract_core_claim, calculate_credibility_score],
)