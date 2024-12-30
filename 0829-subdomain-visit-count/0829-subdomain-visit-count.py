class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)
            
            subdomains = domain.split(".")          
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                domain_count[subdomain] += count

        result = [str(count) + " " + subdomain for subdomain, count in domain_count.items()]
        
        return result