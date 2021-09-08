class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        logs = collections.defaultdict(list)
        for name, time in zip(keyName, keyTime):
            h, m = time.split(':')
            logs[name].append(int(h) * 60 + int(m))

        res = []
        for name, times in logs.items():
            times.sort()
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    res.append(name)
                    break

        return sorted(res)
        