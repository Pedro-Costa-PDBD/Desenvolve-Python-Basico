URLs = ['www.google.com&quot;, www.gmail.com&quot;, www.github.com&quot;, www.reddit.com&quot;, www.yahoo.com&quot;']
print(URLs)
x1 = ["google" if x == "www.google.com&quot;" else "google" for x in URLs]
x2 = ["gmail" if x == "www.gmail.com&quot;" else "gmail" for x in URLs]
x3 = ["github" if x == "www.github.com&quot;" else "github" for x in URLs]
x4 = ["reddit" if x == "www.reddit.com&quot;" else "reddit" for x in URLs]
x5 = ["yahoo" if x == "www.yahoo.com&quot;" else "yahoo" for x in URLs]
URLs = x1 + x2 + x3 + x4 + x5
print(URLs)