system_prompt_strength = f"""
    Let's think step by step. Analyze the CV to provide detailed insights into the candidate's strengths, areas for improvement, and job recommendations. Emphasize identifying the candidate's strengths across various fields, including but not limited to tech, business, HR, and finance.
    For strengths, focus on identifying:
    Core Competencies: Identify the candidate's key skills or areas of expertise relevant to their field. This could include technical proficiencies, such as specific technologies or frameworks, or non-technical skills, such as strategic planning or financial analysis.
    Accomplishments: Highlight significant achievements or projects that showcase the candidate's capabilities. Look for impactful results or successful projects that demonstrate the candidate’s expertise and contributions.
    Leadership and Collaboration: Emphasize any experience in leadership roles, teamwork, or collaborative efforts. Note any roles where the candidate managed teams, led initiatives, or worked effectively with others.
    Problem-Solving and Innovation: Assess examples of how the candidate has addressed challenges or created innovative solutions. Look for creative problem-solving examples or innovative approaches that the candidate has implemented.
    Communication Skills: Detail the candidate's ability to communicate effectively with various stakeholders. Consider their presentation skills, ability to convey complex information, and overall communication proficiency.
    Analytical Skills: Highlight the candidate’s ability to analyze data and make informed decisions. Look for examples of how they have used analytical skills to drive business decisions or improve processes.
    Adaptability and Learning: Describe the candidate's ability to adapt to new situations and learn new skills. Consider how they have handled changes or pursued additional training.
    Client and Customer Focus: Detail the candidate's experience with client or customer interaction and satisfaction. Look for examples of how they have enhanced customer relations or contributed to client success.
    The recommended job roles should align with these strengths, and areas for improvement should help the candidate focus on skill gaps or potential growth areas. Use singular pronouns like "he," "she," "the candidate," or the candidate's name for all comments.
"""

fn_strength_analysis = [
    {
        "name": "AnalyzeCV",
        "description": "Analyze the candidate's resume to assess detailed strengths, areas for improvement, and recommend job roles.",
        "parameters": {
            "type": "object",
            "properties": {
                "strengths": {
                    "type": "object",
                    "properties": {
                        "core_competencies": {
                            "type": "string",
                            "description": "Details specific skills or areas of expertise the candidate excels at, relevant to their field. Examples include: 'Advanced proficiency in data analysis and machine learning' or 'Exceptional skills in project management and team leadership.'"
                        },
                        "accomplishments": {
                            "type": "string",
                            "description": "Highlights significant achievements or projects that showcase the candidate's capabilities. Examples include: 'Successfully launched a new product line that achieved a 25% market share in its first year' or 'Implemented a new recruitment process that decreased hiring time by 30%.'"
                        },
                        "leadership_and_collaboration": {
                            "type": "string",
                            "description": "Details the candidate's experience in leadership roles or collaborative efforts. Examples include: 'Led a team of 10 in a cross-departmental project that improved operational efficiency' or 'Collaborated with senior management to develop and execute a new corporate strategy.'"
                        },
                        "problem_solving_and_innovation": {
                            "type": "string",
                            "description": "Highlights examples of how the candidate has addressed challenges or created innovative solutions. Examples include: 'Developed an innovative marketing strategy that increased brand visibility by 40%' or 'Solved a critical supply chain issue that saved the company $500,000 annually.'"
                        },
                        "communication_skills": {
                            "type": "string",
                            "description": "Details the candidate's ability to effectively communicate with various stakeholders. Examples include: 'Demonstrated excellent presentation skills in high-stakes meetings with clients' or 'Regularly authored clear and concise reports for senior management.'"
                        },
                        "analytical_skills": {
                            "type": "string",
                            "description": "Details the candidate's ability to analyze data and make informed decisions. Examples include: 'Used data analytics to drive business decisions that led to a 15% increase in revenue' or 'Conducted comprehensive financial analyses that improved budgeting accuracy.'"
                        },
                        "adaptability_and_learning": {
                            "type": "string",
                            "description": "Highlights the candidate's ability to adapt to new situations and learn new skills. Examples include: 'Quickly adapted to new project management software and trained team members' or 'Proactively pursued additional training in emerging technologies to stay current in the field.'"
                        },
                        "client_and_customer_focus": {
                            "type": "string",
                            "description": "Details the candidate's experience with client or customer interaction and satisfaction. Examples include: 'Consistently received positive feedback from clients for exceptional service' or 'Developed a customer loyalty program that increased repeat business by 20%.'"
                        }
                    },
                    "description": "A detailed breakdown of the candidate's strongest points in various fields."
                },
                "areas_of_improvement": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Areas where the candidate could improve or skills they lack. e.g., Needs more experience in data-driven decision-making."
                },
                "job_recommended": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Suggested job roles for the candidate based on their profile. e.g., Business Analyst, HR Manager, Financial Advisor."
                }
            },
            "required": [
                "strengths",
                "areas_of_improvement",
                "job_recommended"
            ]
        }
    }
]