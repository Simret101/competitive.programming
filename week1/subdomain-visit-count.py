class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_count = dict()

        for cpdomain in cpdomains:
            count, subdomain = cpdomain.split()
            
            count = int(count)
            domain = subdomain.split(".")
        
            for i in range(len(domain)):
                dom = ".".join(domain[i:])
                domain_count[dom] = domain_count.get(dom, 0) + count

        res = []
        for key, value in domain_count.items():
            res.append("{} {}".format(value, key))

        return res

        