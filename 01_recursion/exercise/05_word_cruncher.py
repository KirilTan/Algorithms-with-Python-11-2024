from typing import List, Dict


class CombinationFinder:
    def __init__(self, elements: List[str], target_word: str):
        """
        Initializes the CombinationFinder with the elements and the target word.
        Also sets up internal data structures for indexing and counting elements.

        Parameters:
            elements (List[str]): List of elements (substrings) to be used to form the target word.
            target_word (str): The word that needs to be formed using combinations of elements.
        """
        self.elements = elements
        self.target_word = target_word
        self.element_indices: Dict[int, List[str]] = {}
        self.element_counts: Dict[str, int] = {}

        # Initialize element indices and counts
        self._initialize_index_and_count()

    def _initialize_index_and_count(self):
        """
        Initializes internal dictionaries to keep track of element indices within the target word
        and the available occurrences of each element.
        """
        # Count occurrences of each element
        for element in self.elements:
            self.element_counts[element] = self.element_counts.get(element, 0) + 1

            # Find all indices where the element appears in the target word
            start_idx = 0
            while True:
                found_idx = self.target_word.find(element, start_idx)
                if found_idx == -1:
                    break

                if found_idx not in self.element_indices:
                    self.element_indices[found_idx] = []
                self.element_indices[found_idx].append(element)

                start_idx = found_idx + len(element)

    def find_all_combinations(self) -> None:
        """
        Public method to start the recursive search for all valid combinations of elements
        that can form the target word.
        """
        self._find_combinations(0, [], "")

    def _find_combinations(
            self,
            index: int,
            current_combination: List[str],
            current_word: str
    ) -> None:
        """
        Recursively finds and prints all combinations of elements that can form the target word.

        Parameters:
            index (int): Current position in the target word being processed.
            current_combination (List[str]): A list storing the current combination of elements used.
            current_word (str): The word formed so far using the current combination.
        """
        if index == len(self.target_word):
            # If the whole target word is successfully formed, print the combination.
            print(' '.join(current_combination))
            return

        if index not in self.element_indices:
            # If no elements start from the current index, return.
            return

        for element in self.element_indices[index]:
            if self.element_counts[element] == 0:
                continue

            current_word += element
            if current_word == self.target_word[:len(current_word)]:
                current_combination.append(element)
                self.element_counts[element] -= 1

                self._find_combinations(
                    index + len(element),
                    current_combination,
                    current_word
                )

                # Backtrack to explore other possibilities
                current_word = current_word[:len(current_word) - len(current_combination[-1])]
                self.element_counts[element] += 1
                current_combination.pop()


if __name__ == "__main__":
    # Input elements and the needed word
    elements = input("Enter elements separated by ', ': ").split(', ')
    target_word = input("Enter the target word: ")

    # Create an instance of CombinationFinder
    combination_finder = CombinationFinder(elements, target_word)

    # Find all combinations
    combination_finder.find_all_combinations()
