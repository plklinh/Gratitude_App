import datetime
from Models.Plan import Plan

from enum import Enum


class EntryType(Enum):
    LOGGED = 1
    DRAFT = 0


class Entry():
    def __init__(self, entryType=None, date=None, gratitude=None, goals=None, plans=None, affirm=None, notes=None):
        self.entryType = entryType
        self.date = date
        self.gratitude = gratitude
        self.goals = goals
        self.plans = plans
        self.affirm = affirm
        self.notes = notes

    def getEntryType(self):
        return "".format(self.entryType.name)

    def setEntryType(self, entryType):
        self.entryType = entryType

    def getDate(self):
        return self.date.strftime("%m/%d/%Y")

    def setDate(self, date):
        self.date = date

    def getGratitude(self):
        gratStr = self.gratitude.join("\n")
        return gratStr

    def setGratitude(self, gratitude):
        self.gratitude = gratitude

    def addGratitudeItem(self, grat):
        self.gratitude.append(grat)

    def deleteGratitudeItem(self, gratToDel):
        self.gratitude.remove(gratToDel)

    def getGoals(self):
        goalsStr = self.goals.join("\n")
        return goalsStr

    def setGoals(self, goals):
        self.goals = goals

    def addGoalItem(self, goal):
        self.goals.append(goal)

    def deleteGoalItem(self, goalToDel):
        self.goals.remove(goalToDel)

    def getPlans(self):
        plansStr = self.plans.__str__().join("\n")
        return plansStr

    def setPlans(self, plans):
        self.plans = plans

    def addPlan(self, plan):
        self.plans.append(plan)

    def deletePlan(self, planToDel):
        self.plans.remove(planToDel)

    def getAffirm(self):
        return self.affirm

    def setAffirm(self, affirm):
        self.affirm = affirm

    def getNotes(self):
        return self.notes

    def setNotes(self, notes):
        self.notes = notes
