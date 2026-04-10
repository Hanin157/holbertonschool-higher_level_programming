#!/usr/bin/python3
"""Simple templating program for invitation generation."""


def generate_invitations(template, attendees):
    """Generate invitation files from a template and attendees data."""
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if attendees == []:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        output = template

        for key in placeholders:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(output)
