class Step():
    def __init__(self, stepDescr=None, status=None) -> None:
        self.stepDes = stepDescr
        self.status = status

    def getDescription(self):
        return "%s" % (self.stepDescr)

    def setDescription(self, stepDescr):
        self.stepDescr = stepDescr

    def getStatus(self, status):
        return "%s" % (self.status)

    def setStatus(self, status):
        self.status = status


class Plan():
    def __init__(self, descr=None, steps=None, status=None):
        self.descr = descr
        self.steps = steps
        self.status = status

    def getDescription(self):
        return "%s" % (self.descr)

    def setDescription(self, descr):
        self.descr = descr

    def getStatus(self):
        return "%s" % (self.status)

    def setDescription(self, status):
        self.status = status

    def getSteps(self):
        return self.steps

    def addStep(self, stepDescr, status):
        newStep = Step(stepDescr, status)
        self.steps.append(newStep)

    def deleteStep(self, stepToDel):
        self.steps.remove(stepToDel)

    def setSteps(self, steps):
        self.steps = steps

    def __str__(self):
        planStr = self.setDescription() + ":"
        for step in self.steps:
            planStr += " \n \t - {des} \t Status: {stat}".format(
                des=step.getDescription(), stat=step.getStatus())
        return planStr
