# UNIVERSITY LIBRARY
university = {
    "school_library": {
        "faculty_of_education": {
            "100_level": {
                "edutech_book_shelf": "Introduction to Educational Technology",
                "special_book_shelf": "Introduction to Inclusive Special Education",
            },
            "400_level": {
                "edutech_book_shelf": "Advanced Educational Technology",
                "special_book_shelf": "Community Leadership",
            },
            "STEM_unit": "Introduction to Programming and Algorithm",
        },

        "faculty_of_science": {
            "chemistry_book_shelf": "Introduction to Organic Chemistry",
            "computer_science_book_shelf": "Machine Learning and AI"
        },

        "faculty_of_art": {
            "history_book_shelf": "Introduction to Organic Chemistry",
            "CLA_book_shelf": "Machine Learning and AI"
        },

        "faculty_of_social_science": {
            "psychology_book_shelf": "Introduction to Organic Chemistry",
            "sociology_science_book_shelf": "Machine Learning and AI"
        },

        "faculty_of_technology": {
            "AI_book_shelf": "Introduction to AI for Social Good",
            "computer_science_book_shelf": "Machine Learning and AI"
        },
    },

    "clinic": {
        "admin_desk": {
        }
    }
}

print("\nSORTING BOOKS IN LIBRARY\n======================")
for school in university:
    if school != "faculty_of_education":
        print("Not in the University")
