# system_prompt_weakness = f"""
# Let's think step by step.
# Analyze the CV to detect specific weaknesses or areas where the candidate's profile can be improved. Focus on identifying:
# - Gaps in technical skills: Pinpoint any missing or outdated technical skills, including specific technologies or tools the candidate should be proficient in for their field.
# - Lack of measurable accomplishments: Highlight the absence of quantifiable achievements, KPIs, or impact from the candidate's previous roles.
# - Insufficient details: Detect areas where the candidate's descriptions of responsibilities, projects, or achievements are too vague or lack context.
# - Leadership and teamwork gaps: Identify if the candidate lacks leadership experience or does not provide examples of teamwork and collaboration in their previous roles.
# - Career inconsistency: Point out inconsistencies such as frequent job changes, lack of career progression, or gaps in employment that may raise concerns.
# - Formatting or structural issues: Highlight problems with the CV format, such as missing sections, unclear structure, or poor use of white space, which may make the CV difficult to read or understand.
# Provide specific feedback for each weakness and suggestions for improvement.
# """

# fn_weakness_detection = [
#     {
#         "name": "DetectWeaknesses",
#         "description": "Analyze the candidate's resume to identify detailed weaknesses or areas of improvement.",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "technical_gaps": {
#                     "type": "array",
#                     "items": {
#                         "type": "object",
#                         "properties": {
#                             "missing_technologies": {
#                                 "type": "string",
#                                 "description": "Specific technologies or tools that the candidate is missing based on the job role or field they are aiming for. e.g., 'The candidate has no experience with modern cloud platforms such as AWS, GCP, or Azure.'",
#                             },
#                             "outdated_skills": {
#                                 "type": "string",
#                                 "description": "Technologies or tools the candidate is using that are no longer in demand or have been replaced by more modern solutions. e.g., 'The candidate is still using jQuery instead of modern JavaScript frameworks like React or Vue.'",
#                             },
#                             "missing_certifications": {
#                                 "type": "string",
#                                 "description": "Relevant certifications the candidate could pursue to enhance their technical profile. e.g., 'Lacks certifications in data analytics or machine learning, which could strengthen the profile for AI-related roles.'",
#                             },
#                         },
#                     },
#                     "description": "Detailed analysis of the candidate's gaps in technical skills or proficiencies.",
#                 },
#                 "lack_of_accomplishments": {
#                     "type": "string",
#                     "description": "Specific examples of where the candidate's CV lacks measurable outcomes or achievements. e.g., 'The candidate lists responsibilities but does not provide any quantified results, such as increasing sales by X% or reducing system downtime by Y%.'",
#                 },
#                 "vague_descriptions": {
#                     "type": "array",
#                     "items": {
#                         "type": "object",
#                         "properties": {
#                             "unclear_projects": {
#                                 "type": "string",
#                                 "description": "Projects listed without sufficient detail. e.g., 'The candidate mentions developing a web application but does not specify the technologies used or the outcome of the project.'",
#                             },
#                             "unclear_responsibilities": {
#                                 "type": "string",
#                                 "description": "Job responsibilities that are described too broadly without explaining specific tasks or outcomes. e.g., 'Responsibilities include managing a team, but there is no explanation of how many team members or what tasks were managed.'",
#                             },
#                         },
#                     },
#                     "description": "Detailed points where the candidate's descriptions of their roles, projects, or responsibilities are too vague.",
#                 },
#                 "leadership_gaps": {
#                     "type": "string",
#                     "description": "Examples where the candidate lacks evidence of leadership or teamwork. e.g., 'No mention of any leadership roles, even though the candidate has been in the field for 5 years.'",
#                 },
#                 "career_inconsistency": {
#                     "type": "array",
#                     "items": {
#                         "type": "object",
#                         "properties": {
#                             "frequent_job_changes": {
#                                 "type": "string",
#                                 "description": "Indicates if the candidate frequently switches jobs without clear career advancement. e.g., 'The candidate has changed jobs every year for the last 5 years without significant promotion or progression.'",
#                             },
#                             "employment_gaps": {
#                                 "type": "string",
#                                 "description": "Detects gaps in employment that are not explained. e.g., 'There is a two-year gap in employment without any explanation provided.'",
#                             },
#                         },
#                     },
#                     "description": "Highlights inconsistencies in the candidate's career progression or gaps in employment.",
#                 },
#                 "cv_format_issues": {
#                     "type": "array",
#                     "items": {
#                         "type": "object",
#                         "properties": {
#                             "missing_sections": {
#                                 "type": "string",
#                                 "description": "Identifies key sections that are missing from the CV, such as education, certifications, or technical skills. e.g., 'The CV does not include a section on technical skills or relevant certifications.'",
#                             },
#                             "poor_structure": {
#                                 "type": "string",
#                                 "description": "Highlights structural issues with the CV layout. e.g., 'The CV uses inconsistent font sizes and lacks clear section headings, making it difficult to navigate.'",
#                             },
#                             "unbalanced_content": {
#                                 "type": "string",
#                                 "description": "Indicates if the CV overemphasizes certain sections while neglecting others. e.g., 'The candidate's CV focuses heavily on education but provides very little detail about work experience.'",
#                             },
#                         },
#                     },
#                     "description": "Points out issues with the CV format, structure, or balance of content.",
#                 },
#             },
#             "required": [
#                 "technical_gaps",
#                 "lack_of_accomplishments",
#                 "vague_descriptions",
#                 "leadership_gaps",
#                 "career_inconsistency",
#                 "cv_format_issues",
#             ],
#         },
#     }
# ]

# system_prompt_weakness = f"""
system_prompt_weakness = f"""
Let's carefully analyze the candidate's resume for specific weaknesses and areas for improvement. For each category, provide detailed feedback, and if certain information isn't detected, suggest what could be added to improve the resume. Fill in the following fields:

1. **Skills and Qualifications**:
   - Identify any missing or outdated skills relevant to the candidate's field. Suggest certifications if relevant.
   
   "missing_skills": If no missing skills are detected, provide suggestions for enhancing the skills list.
   "outdated_skills": Highlight any outdated skills or technologies.
   "relevant_certifications": Recommend any certifications the candidate could pursue.

2. **Impact and Achievements**:
   - Review the resume for measurable accomplishments, like KPIs, and provide specific suggestions to add quantifiable achievements if missing.
   
   "impact_and_achievements": If the candidate lacks quantifiable achievements, suggest examples such as "Improved sales by 20%," or "Reduced costs by 10%."

3. **Clarity of Descriptions**:
   - Examine the clarity of responsibilities and projects described in the resume.
   
   "vague_responsibilities": Highlight vague or unclear job responsibilities. Suggest adding more specific details where needed.
   "vague_projects": Point out any project descriptions that lack details or context. Provide suggestions for improvement.

4. **Leadership and Collaboration**:
   - Determine whether leadership and teamwork examples are well represented.
   
   "leadership_and_collaboration": If leadership and teamwork examples are lacking, suggest how the candidate can demonstrate these traits, even if through side projects or volunteer work.

5. **Career Trajectory**:
   - Analyze for job-hopping or employment gaps, and suggest ways to address these concerns.

   "job_hopping": Highlight frequent job changes or career instability if present.
   "employment_gaps": Point out unexplained gaps in employment, and recommend ways to address them.

6. **Resume Formatting**:
   - Identify issues with the structure, format, or missing sections of the resume.
   
   "formatting_issues": Describe any formatting issues that make the resume difficult to read.
   "missing_sections": Highlight if key sections (like education, skills, or experience) are missing.

For each section, provide actionable suggestions on how the candidate can improve their resume, even if no significant weaknesses are detected.
"""

# """


fn_weakness_detection = [
    {
        "name": "AnalyzeResumeWeaknesses",
        "description": "Generalized analysis of a candidate's resume to identify key weaknesses or areas for improvement.",
        "parameters": {
            "type": "object",
            "properties": {
                "skills_and_qualifications": {
                    "type": "object",
                    "properties": {
                        "missing_skills": {
                            "type": "string",
                            "description": "Skills or qualifications that the candidate lacks, relative to the job or industry requirements.",
                        },
                        "outdated_skills": {
                            "type": "string",
                            "description": "Skills or tools listed that are no longer in demand.",
                        },
                        "relevant_certifications": {
                            "type": "string",
                            "description": "Certifications or formal qualifications missing from the resume that are important for the candidate's field."
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "Analysis of the candidate's skills and qualifications with suggestions for improvement. Encourage the candidate to gain new skills, update outdated skills, or pursue certifications that can enhance their profile."
                        }
                    },
                },
                "impact_and_achievements": {
                    "type": "object",
                    "properties": {
                        "issue": {
                            "type": "string",
                            "description": "Specific examples where the resume lacks measurable results or accomplishments, such as KPIs or key outcomes from previous roles.",
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "Recommend the candidate add measurable achievements, such as 'increased sales by 15%' or 'reduced processing time by 30%.'"
                        }
                    } 
                },
                "clarity_of_descriptions": {
                    "type": "object",
                    "properties": {
                        "vague_responsibilities": {
                            "type": "string",
                            "description": "Responsibilities listed that are too general or lack specific detail."
                        },
                        "vague_projects": {
                            "type": "string",
                            "description": "Projects described without sufficient context, tools used, or results achieved."
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "Analysis of areas where the candidate's descriptions are unclear or lack detail. Encourage the candidate to be more specific about their roles, technologies used, and the impact of their contributions.",
                        }
                    },
                },
                "leadership_and_collaboration": {
                    "type": "object",
                    "properties": {
                        "issue": {
                            "type": "string",
                            "description": "Identify if the candidate lacks evidence of leadership, teamwork, or collaboration experience."
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "Suggest highlighting teamwork and leadership roles, even if informal, or adding examples of collaboration in various projects."
                        }
                    }
                },
                "career_trajectory": {
                    "type": "object",
                    "properties": {
                        "job_hopping": {
                            "type": "string",
                            "description": "Detect frequent job changes without clear career advancement."
                        },
                        "employment_gaps": {
                            "type": "string",
                            "description": "Gaps in employment history that are not explained or accounted for."
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "Identify issues in the candidate’s career progression or any unexplained employment gaps. Encourage explaining gaps and frequent job changes by framing them positively, such as skill development during breaks or growth achieved through different roles.",
                        }
                    },
                },
                "resume_formatting": {
                    "type": "object",
                    "properties": {
                        "formatting_issues": {
                            "type": "string",
                            "description": "General formatting issues that make the resume difficult to read or understand, such as poor structure or inconsistent use of fonts and spacing."
                        },
                        "missing_sections": {
                            "type": "string",
                            "description": "Important sections that are missing, such as education, skills, or relevant work experience."
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "Analysis of formatting or structural problems in the resume. Suggest improving the layout with clear headings, consistent formatting, and ensuring that all key sections (skills, experience, education) are included."
                        }
                    },
                }
            },
            "required": [
                "skills_and_qualifications",
                "impact_and_achievements",
                "clarity_of_descriptions",
                "leadership_and_collaboration",
                "career_trajectory",
                "resume_formatting"
            ]
        }
    }
]
