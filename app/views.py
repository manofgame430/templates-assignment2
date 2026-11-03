from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

leadership = {"team": ["procurement", "management", "community", "documentation"],
              "teams": {
                  "procurement": {
                      "description": "The procurment team is in charge of working within a limited budget in order to create fulfilling and nutritous meals that adhere to everyones dietery needs and restrictions.",
                      "members": ["Christopher", "Tristan", "Brian"],
                  },
                  "management": {
                      "description": "The managment team is in charge of managing the other teams, ensuring communication between teams, assigning roles to each team, and ensuring cleaning duties are assigned and completed.",
                      "members": ["Christopher", "Tristan", "Brian"],
                  },
                  "documentation": {
                      "description": "The documentation team is in charge of managing basecamp's social media pages and also documenting major milestones like birthdays and team introductions.",
                      "members": ["Germaine", "Tyler-Vincent", "Tyler-Joy", "Corey"],
                  },
                  "community": {
                      "description": "The community team is in charge of planning, organizing, and executing events that help everyone bond with each other.",
                      "members": ["Germaine", "Tyler-Vincent", "Tyler-Joy", "Corey"],
                  },                 
              }}


# Create your views here.
def home_view(request:HttpRequest)->HttpResponse:
    context = {"teams": leadership["team"]}
    return render(request, 'base.html', context)


def team_view(request:HttpRequest, team)->HttpRequest:
    context = {"teams": leadership["teams"], 
               "team": leadership["team"],
               "id": team}
    return render(request, 'team.html', context)



def procurment_view(request:HttpRequest)->HttpResponse:
    context = {"members": ["Christopher", "Tristan", "Brian"]}
    return render(request, 'procurment.html', context)

def management_view(request:HttpRequest)->HttpResponse:
    context = {"members": ["Christopher", "Tristan", "Brian"]}
    return render(request, 'management.html', context)

def community_view(request:HttpRequest)->HttpResponse:
    context = {"members": ["Germaine", "Tyler-Vincent", "Tyler-Joy", "Corey"]}
    return render(request, 'community.html', context)

def documentation_view(request:HttpRequest)->HttpResponse:
    context = {"members": ["Germaine", "Tyler-Vincent", "Tyler-Joy", "Corey"]}
    return render(request, 'documentation.html', context)