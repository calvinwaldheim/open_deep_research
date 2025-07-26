"""
Architecture-specific prompts and research templates for optimized trend report generation.
These prompts are designed to improve the quality and relevance of architecture trend reports.
"""

# Enhanced research topic transformation for architecture
architecture_research_topic_prompt = """You will be given a set of messages about an architecture trend report request. 
Your job is to translate these messages into a detailed, architecture-focused research question.

The messages that have been exchanged so far between yourself and the user are:
<Messages>
{messages}
</Messages>

Today's date is {date}.

You will return a single research question optimized for architecture industry research.

**Architecture-Specific Guidelines:**

1. **Industry Focus - Always Include:**
   - Specify "sustainable architecture", "green building", "eco-friendly design" if sustainability is mentioned
   - Include building types: residential, commercial, institutional, industrial, mixed-use
   - Consider construction methods: prefab, modular, traditional, innovative materials
   - Include design philosophies: biophilic design, minimalism, maximalism, brutalism, etc.

2. **Location Context - Be Specific:**
   - Include climate considerations (temperate, tropical, arid, cold)
   - Consider local building codes and regulations
   - Include regional architectural styles and cultural influences
   - Factor in local material availability and labor practices

3. **Temporal Scope - Define Clearly:**
   - Specify if looking at current trends (2024-2025) vs emerging trends (2025-2030)
   - Include seasonal considerations if relevant
   - Consider market cycles and economic factors

4. **Technical Aspects - Include:**
   - Building technologies: smart home systems, energy efficiency, renewable energy integration
   - Material innovations: new composites, recycled materials, bio-based materials
   - Construction techniques: 3D printing, AI-assisted design, virtual reality planning

5. **Market Dynamics - Consider:**
   - Client preferences and demographics
   - Budget ranges (luxury, mid-market, affordable housing)
   - Regulatory changes and policy impacts
   - Real estate market conditions

6. **Sources Priority - Architecture-Specific:**
   - Professional architecture publications (Architectural Digest, ArchDaily, Dezeen)
   - Industry organizations (AIA, RIBA, Green Building Council)
   - Construction industry reports and trade publications
   - Academic architecture and urban planning journals
   - Government building and planning department publications

**Example Enhanced Research Questions:**

Instead of: "What are architecture trends for 2025?"
Better: "What are the top 5 sustainable residential architecture trends for 2025 in temperate North American climates, focusing on energy-efficient design, innovative materials, and smart home integration that appeal to millennial homebuyers in the $300K-$800K market range?"

Instead of: "What's trending in commercial buildings?"
Better: "What are the most significant post-pandemic commercial office building design trends for 2024-2025, specifically focusing on flexible workspace solutions, indoor air quality improvements, and biophilic design elements that support hybrid work models in major US metropolitan areas?"

Transform the user's request into a comprehensive, architecture-focused research question that will yield high-quality, specific, and actionable trend insights.
"""

# Architecture-specific research instructions for individual researchers
architecture_research_instructions = """You are conducting research specifically for an architecture trend report. 

**Research Focus Areas:**
1. **Design Trends:** Current and emerging aesthetic preferences, spatial arrangements, and design philosophies
2. **Material Innovations:** New building materials, sustainable options, performance characteristics
3. **Technology Integration:** Smart building systems, energy efficiency, automation, AR/VR in design
4. **Sustainability:** Green building practices, LEED standards, carbon neutrality, renewable energy
5. **Regulatory Changes:** Building codes, zoning updates, accessibility requirements
6. **Market Drivers:** Economic factors, demographic shifts, lifestyle changes affecting architecture

**Search Strategy:**
- Start with industry-specific publications and professional organizations
- Look for case studies and real project examples
- Include cost analysis and ROI data when available
- Search for regional variations and local adaptations
- Find expert quotes from practicing architects and industry leaders

**Quality Indicators to Look For:**
- Recent publication dates (2023-2025 preferred)
- Credible sources (established firms, industry publications, academic research)
- Specific project examples with photos/plans
- Quantitative data (market size, adoption rates, cost figures)
- Expert commentary and professional opinions

**Information to Prioritize:**
- Practical implementation details
- Cost implications and budget considerations
- Timeline for adoption (near-term vs long-term trends)
- Geographic variations and local considerations
- Client/user satisfaction and feedback

Remember: Architecture trends must be actionable and relevant for practicing architects and their clients.
"""

# Enhanced final report template for architecture trends
architecture_report_template = """Based on all the research conducted, create a comprehensive architecture trend report that answers:
<Research Brief>
{research_brief}
</Research Brief>

Today's date is {date}.

Here are the findings from the research:
<Findings>
{findings}
</Findings>

**Structure your architecture trend report with these sections:**

# [Report Title] - Architecture Trends Report

## Executive Summary
- 2-3 sentence overview of key findings
- Top 3-5 most significant trends identified
- Timeline and adoption outlook

## 1. Current Market Landscape
- Industry overview and market size
- Key drivers influencing architectural decisions
- Economic and regulatory factors

## 2. Top Architecture Trends

### Trend 1: [Specific Trend Name]
- **Description:** What is this trend?
- **Key Features:** Specific design elements, materials, or technologies
- **Examples:** Real projects demonstrating this trend (with project names and locations)
- **Benefits:** Why clients/users are adopting this
- **Implementation:** Practical considerations for architects
- **Cost Impact:** Budget implications (higher/lower/similar costs)
- **Timeline:** Current adoption level and growth projection

### Trend 2: [Specific Trend Name]
[Same structure as above]

### [Continue for 3-5 major trends]

## 3. Regional Variations
- How trends differ by location/climate
- Local adaptations and cultural influences
- Regulatory differences affecting implementation

## 4. Technology & Innovation
- Emerging technologies impacting design
- Material innovations and new products
- Digital tools changing the design process

## 5. Sustainability Focus
- Environmental considerations driving trends
- Green building standards and certifications
- Energy efficiency and renewable energy integration

## 6. Market Outlook & Predictions
- Which trends are likely to grow
- Emerging trends to watch for next year
- Potential challenges and barriers

## 7. Implementation Recommendations
- **For Architects:** How to incorporate trends into practice
- **For Clients:** What to expect in terms of costs and timelines
- **For Developers:** Market positioning and competitive advantages

## Sources
[All referenced links in format: [Title](URL)]

**Writing Guidelines:**
- Use specific project examples whenever possible
- Include quantitative data (percentages, costs, timelines)
- Reference expert quotes from practicing architects
- Make recommendations actionable and practical
- Focus on trends with real market traction, not just concepts
- Consider both residential and commercial applications
- Include high-end and affordable market segments
"""

# Location-specific research enhancement
location_based_research_prompt = """When researching architecture trends for {location}, consider these location-specific factors:

**Climate Considerations:**
- Local weather patterns and seasonal variations
- Natural disaster risks (earthquakes, hurricanes, floods)
- Energy efficiency requirements for the climate
- Outdoor living space needs and preferences

**Cultural & Regulatory Context:**
- Local architectural heritage and preferred styles
- Building codes and zoning regulations specific to the area
- Historic preservation requirements
- Accessibility and inclusivity standards

**Market Dynamics:**
- Local real estate market conditions
- Typical budget ranges for residential/commercial projects
- Popular neighborhoods and development areas
- Demographic preferences (families, young professionals, retirees)

**Material & Labor Considerations:**
- Locally available building materials
- Regional construction labor practices
- Transportation costs for imported materials
- Local supplier and contractor capabilities

**Economic Factors:**
- Local cost of living and construction costs
- Economic growth or decline affecting building activity
- Government incentives for certain types of construction
- Tax implications for different building approaches

Research should prioritize sources and examples specifically relevant to {location} while also drawing insights from similar climates and markets globally.
""" 