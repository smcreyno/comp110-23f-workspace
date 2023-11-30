"""Function writing practice."""


class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, pr: str) -> bool:
        """Checks if course is 400+ and if prereqs list contains prereq."""
        if self.level >= 400:
            for p in self.prerequisites:
                if p == pr:
                    return True
        else:
            return False
    

def find_courses(courses: list[Course], prereq: str) -> list[str]:
    """Finds the names of courses whose level is 400+ and has the prereqs."""
    names: list[str] = []
    for c in courses:
        if c.level >= 400:
            for p in c.prerequisites:
                if prereq == p:
                    names.append(c.name)
    