class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")

        lenV1 = len(version1)
        lenV2 = len(version2)
        maxLength = max(lenV1, lenV2)

        for i in range(maxLength):
            v1 = int(version1[i]) if i < lenV1 else 0
            v2 = int(version2[i]) if i < lenV2 else 0

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return 0
