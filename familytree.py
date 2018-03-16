

def family_tree(namelist):
    name = []
    for ((dad, mom), child) in namelist:
        if not name:
            name.append([dad, mom])
            name.append([child])
        else:
            for index in range(len(name)):
                if child in name[index]:
                    name.insert(index, [dad, mom])
                    break
                elif mom in name[index]:
                    if index == len(name) - 1:
                        name.append([child])
                    else:
                        name[index + 1].append(child)
                    if dad not in name[index]:
                        name[index].append(dad)
                    break

                elif dad in name[index]:
                    if index == len(name) - 1:
                        name.append([child])
                    else:
                        name[index + 1].append(child)
                    if mom not in name[index]:
                        name[index].append(mom)
                    break

        return name


if __name__ == '__main__':
    family_tree([(['A', 'C'], 'B'), (['B', 'D'], 'E'), (['D', 'F'], 'G')])
