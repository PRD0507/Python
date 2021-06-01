
class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, check):
        spaces = ' ' * self.get_level()
        prefix = spaces + "|__" if self.parent else ""

        if check == 'both':
            print(prefix, self.name, "(", self.designation, ")")
        elif check == 'name':
            print(prefix, self.name)
        else:
            print(prefix, self.designation)

        if self.children:
            for child in self.children:
                child.print_tree(check)

def build_management_tree():
    root = TreeNode("Nipul", "CEO")

    chinmay = TreeNode("Chinmay", "CTO")
    vishwa = TreeNode("Vishwa", "Infrastructure Head")
    chinmay.add_child(vishwa)
    chinmay.add_child(TreeNode("Amir", "Application Head"))

    vishwa.add_child(TreeNode("Dhaval", "Cloud Manager"))
    vishwa.add_child(TreeNode("Abhijit", "App Manager"))

    gels = TreeNode("Gels", "HR Head")
    gels.add_child(TreeNode("Peter", "Recruitment Manager"))
    gels.add_child(TreeNode("Waqar", "Policy Manager"))

    root.add_child(chinmay)
    root.add_child(gels)

    return root



if __name__ == '__main__':
    root =  build_management_tree()
    root.print_tree("both")
    root.print_tree("name")
    root.print_tree("designation")


