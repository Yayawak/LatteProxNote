from Chapters.Introduction.IntroductionWidget import IntroductionWidget
from Chapters.Introduction.ImageProjectionCanvas import ImageProjectionCanvas

indexing = {
    # "introduction" : IntroductionWidget()
    "introduction" :
        {
            "prolog" : IntroductionWidget(),
            "sections" : {
                "mapping real world to image plane" : ImageProjectionCanvas()
            }
        }
}
class Caller:
    def __init__(self):
        ...
        Duolity(prolog, sections)
    # def

class Duolity:
    def __init__(self, prolog, sections):
        self.prolog = prolog
        self.sections = sections
