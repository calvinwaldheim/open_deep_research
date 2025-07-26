"""
Architecture-specific configuration and research customizations.
This module provides specialized research behavior for architecture trend reports.
"""

from .architecture_prompts import (
    architecture_research_topic_prompt,
    architecture_research_instructions,
    architecture_report_template,
    location_based_research_prompt
)

class ArchitectureResearchConfig:
    """Configuration class for architecture-specific research behavior."""
    
    def __init__(self, location=None, year=None, industry_focus=None):
        self.location = location or "United States"
        self.year = year or 2025
        self.industry_focus = industry_focus or "Architecture & Construction"
        
    def get_enhanced_research_prompt(self, messages, date):
        """Get architecture-specific research topic transformation prompt."""
        base_prompt = architecture_research_topic_prompt.format(
            messages=messages, 
            date=date
        )
        
        if self.location and self.location != "Global":
            location_enhancement = location_based_research_prompt.format(
                location=self.location
            )
            return f"{base_prompt}\n\n{location_enhancement}"
        
        return base_prompt
    
    def get_research_instructions(self):
        """Get architecture-specific research instructions for individual researchers."""
        return architecture_research_instructions
    
    def get_report_template(self, research_brief, findings, date):
        """Get architecture-specific report template."""
        return architecture_report_template.format(
            research_brief=research_brief,
            findings=findings,
            date=date
        )
    
    def get_search_keywords_enhancement(self, base_query):
        """Enhance search queries with architecture-specific keywords."""
        architecture_keywords = [
            "architecture trends",
            "building design",
            "construction innovation",
            "sustainable architecture",
            "green building",
            "smart buildings",
            "architectural materials",
            "design trends",
            "building technology",
            "energy efficiency",
            "LEED certification",
            "biophilic design",
            "modular construction",
            "prefab architecture"
        ]
        
        # Add location-specific terms if specified
        if self.location and self.location != "Global":
            location_terms = [
                f"{self.location} architecture",
                f"{self.location} building codes",
                f"{self.location} construction trends",
                f"{self.location} real estate"
            ]
            architecture_keywords.extend(location_terms)
        
        # Add year-specific terms
        year_terms = [
            f"{self.year} architecture trends",
            f"{self.year} building trends",
            f"{self.year} construction trends"
        ]
        architecture_keywords.extend(year_terms)
        
        return {
            "enhanced_query": f"{base_query} {' '.join(architecture_keywords[:5])}",
            "fallback_queries": [
                f"{base_query} architecture design trends {self.year}",
                f"{base_query} building construction innovation {self.location}",
                f"{base_query} sustainable architecture {self.year}",
                f"{base_query} smart building technology trends"
            ]
        }
    
    def get_source_priorities(self):
        """Define priority sources for architecture research."""
        return {
            "primary_sources": [
                "archidaily.com",
                "dezeen.com", 
                "architecturaldigest.com",
                "architecturalrecord.com",
                "metropolismag.com",
                "aia.org",
                "usgbc.org",
                "construction.com",
                "bdcnetwork.com",
                "greenbuildingadvisor.com"
            ],
            "secondary_sources": [
                "archdaily.com",
                "designboom.com",
                "inhabitat.com",
                "treehugger.com",
                "constructiondive.com",
                "buildinggreendigital.com",
                "contractormag.com",
                "constructionexec.com"
            ],
            "academic_sources": [
                "sciencedirect.com",
                "scholar.google.com",
                "researchgate.net",
                "ieee.org",
                "journals.sagepub.com"
            ]
        }
    
    def get_quality_filters(self):
        """Define quality filters for architecture research."""
        return {
            "required_keywords": [
                "architecture", "building", "design", "construction", 
                "sustainable", "trends", "innovation", "technology"
            ],
            "preferred_date_range": {
                "start_year": self.year - 2,
                "end_year": self.year + 1
            },
            "exclude_patterns": [
                "listicle", "top 10", "clickbait", "advertisement",
                "sponsored content", "press release"
            ],
            "minimum_content_length": 500,  # words
            "required_elements": [
                "specific examples",
                "expert quotes",
                "quantitative data",
                "project details"
            ]
        }
    
    def get_validation_criteria(self):
        """Define validation criteria for architecture trend reports."""
        return {
            "content_requirements": {
                "minimum_trends": 3,
                "minimum_examples_per_trend": 2,
                "minimum_sources": 10,
                "required_sections": [
                    "Executive Summary",
                    "Current Market Landscape", 
                    "Top Architecture Trends",
                    "Implementation Recommendations",
                    "Sources"
                ]
            },
            "quality_indicators": {
                "specific_project_examples": True,
                "cost_information": True,
                "timeline_projections": True,
                "expert_quotes": True,
                "quantitative_data": True,
                "regional_considerations": True
            },
            "technical_depth": {
                "material_specifications": True,
                "technology_details": True,
                "implementation_challenges": True,
                "regulatory_considerations": True
            }
        }

# Factory function to create architecture-specific configuration
def create_architecture_config(location=None, year=None, industry_focus=None):
    """Create an architecture research configuration with optional parameters."""
    return ArchitectureResearchConfig(
        location=location,
        year=year, 
        industry_focus=industry_focus
    )

# Integration helper for the main research system
def enhance_research_for_architecture(base_config, arch_config):
    """Enhance the base research configuration with architecture-specific settings."""
    
    # This would be called during research initialization to modify prompts and behavior
    enhancements = {
        "specialized_prompts": {
            "research_topic_transform": arch_config.get_enhanced_research_prompt,
            "research_instructions": arch_config.get_research_instructions(),
            "report_template": arch_config.get_report_template
        },
        "search_enhancements": {
            "keyword_expansion": arch_config.get_search_keywords_enhancement,
            "source_priorities": arch_config.get_source_priorities(),
            "quality_filters": arch_config.get_quality_filters()
        },
        "validation_criteria": arch_config.get_validation_criteria()
    }
    
    return enhancements 