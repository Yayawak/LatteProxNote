import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib as mpl


class ConnectedComponentLabeling:
    def __init__(self):
        size = (6, 6)
        # size = (10, 10)
        # np.random.seed(0)
        # self.img = np.random.randint(0, 2, size=size)
        self.img = np.random.choice([0, 1], size=size)
        self.labelImg = np.zeros_like(self.img)
        print(self.img)

        # self.equivalentTable = set()
        self.equivalentTable = []

        # plt.imshow(self.img, cmap='gray')
        # print(self.labelImg)
        # print("is [-1,2] out of bound : ",  self.checkIsOutOfBound(-1, 2))
        print()
        self.labelPixel()
        print(self.labelImg)
        print("equiv table")
        # self.equivalentTable = list(set(self.equivalentTable))
        # self.equivalentSet = set(map(frozenset, self.equivalentTable))
        print(self.equivalentTable)
        print()

        print("equiv set")
        # print(self.equivalentSet)
        print()

        print("eqv set !")
        print(self.getEquivalentSet())

        print("relabeling")
        self.relabel()
        print(self.labelImg)

        fig, axs = plt.subplots(ncols=2, figsize=[8,8])
        axs[0].imshow(self.img, cmap='gray')
        axs[1].imshow(self.labelImg, cmap='inferno')
        # print()
        plt.show()

    def getEquivalentSet(self):
        # equivalent_list = [list(subset) for subset in self.equivalentTable]
        # final_list = []
        # for subset in equivalent_list:
        #     merged = False
        #     for i, existing_subset in enumerate(final_list):
        #         if any(label in existing_subset for label in subset):
        #             final_list[i] = list(set(existing_subset)
        #                 | set(subset))
        #             merged = True
        #             break
        #     if not merged:
        #         final_list.append(subset)
        # return [list(set(subset)) for subset in final_list]
        G = nx.Graph()

        equivalent_list = [list(subset) for subset in self.equivalentTable]
        for subset in equivalent_list:
            G.add_edge(subset[0], subset[1])
        connected_component = nx.connected_components(G)
        output_list = [list(component) for component in connected_component]
        return output_list
        # pos = nx.spring_layout(G)
        # nx.draw(G, pos, with_labels=True)
        # plt.show()

    def relabel(self):
        # equivalentDict = {}
        # for equivalent_labels in self.equivalentSet:
        #     root_label = min(equivalent_labels)
        #     for label in equivalent_labels:
        #         equivalentDict[label] = root_label
        # print("equivalent Dict !!")
        # print(equivalentDict)
        # for i in range(self.labelImg.shape[0]):
        #     for j in range(self.labelImg.shape[1]):
        #         if self.labelImg[i, j] != 0:
        #             self.labelImg[i, j] = equivalentDict[self.labelImg[i, j]]
        # ? v2
        # equivalent_list = [list(subset) for subset in self.equivalentSet]
        # print("eqv list")
        # print(equivalent_list)
        # # unique_labels = sorted(set(label for subset in equivalent_list
        # #     for label in subset))
        # # print("unique label")
        # # print(unique_labels)
        # print()
        # final_list = []
        # for subset in equivalent_list:
        #     if not any(set(subset).issubset(s) for s in final_list):
        #         final_list.append(subset)

        # print("final list")
        # print(final_list)
        # ? v3
        equivalent_set = self.getEquivalentSet()
        # for subset in equivalent_set:
        #     for label in subset:
        for i in range(self.labelImg.shape[0]):
            for j in range(self.labelImg.shape[1]):
                color = self.labelImg[i, j]
                if color != 0:
                    for sub_list in equivalent_set:
                        if set([color]).issubset(set(sub_list)):
                            self.labelImg[i, j] = min(sub_list)

    def labelPixel(self):
        label: int = 0
        leftLabeled: bool = False
        topLabeled: bool = False

        for i in range(self.img.shape[0]):
            for j in range(self.img.shape[1]):
                if (self.img[i, j] == 1):
                    leftLabeled = self.labelImg[i - 1, j] != 0
                    topLabeled = self.labelImg[i, j - 1] != 0
                    # ? Some of left, top already have label
                    if (topLabeled):
                        self.labelImg[i, j] = self.labelImg[i, j - 1]
                    elif (leftLabeled):
                        self.labelImg[i, j] = self.labelImg[i - 1, j]
                    if (leftLabeled and topLabeled):
                        # ? Both have the same label
                        if (self.labelImg[i - 1, j]
                                == self.labelImg[i, j - 1]):
                            self.labelImg[i, j] = self.labelImg[i - 1, j]
                        # ? Both have diff label
                        else:
                            self.labelImg[i, j] = self.labelImg[i, j - 1]
                            self.equivalentTable.append([
                                self.labelImg[i - 1, j],
                                self.labelImg[i, j - 1],
                            ])
                    # ? no left, no right both
                    if (not leftLabeled and not topLabeled):
                        label += 1
                        self.labelImg[i, j] = label
                        self.equivalentTable.append([
                            self.labelImg[i, j],
                            self.labelImg[i, j],
                        ])

    def isOutOfBound(self, x, y):
        if (y < 0 or y > len(self.img) - 1):
            return True
        if (x < 0 or x > len(self.img[0] - 1)):
            return True
        return False
