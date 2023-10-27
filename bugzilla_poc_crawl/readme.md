主旨：直接爬包含CVE字符串的

***

筛选策略：

1. **Status:** VERIFIED, CLOSED
2. **Summary:** CVE

总共有59626个数据

***

字段;

1. 关键词都爬上
2. attachment
3. comment

如果有attachment单独存储为文件，在描述里面的就不管了

***

10.5 

直接爬发现table是没有的，那只能试试API的思路

***

VERIFIED----QA已经查看过bug的解决方案,并且同意针对bug已经做出的修改。

CLOSED----bug已经被解决,解决方案是被认为是正确的

<a class="bz_bug_link bz_CLOSED bz_unspecified bz_unspecified bz_closed bz_public" title="CVE-2010-0010 httpd (v1.3): mod_proxy overflow on 64-bit systems" href="show_bug.cgi?id=561358">561358</a>

```
https://bugzilla.redhat.com/buglist.cgi?bug_status=VERIFIED&bug_status=CLOSED&columnlist=product%2Ccomponent%2Cassigned_to%2Cstatus%2Csummary%2Clast_change_time%2Cseverity%2Cpriority&list_id=13345061&order=priority%2C%20severity%2C%20&query_format=advanced&short_desc=CVE&short_desc_type=allwordssubstr

https://bugzilla.redhat.com/buglist.cgi?bug_status=VERIFIED&bug_status=CLOSED&columnlist=product%2Ccomponent%2Cassigned_to%2Cstatus%2Csummary%2Clast_change_time%2Cseverity%2Cpriority&list_id=13345061&order=priority%2C%20severity%2C%20&query_format=advanced&short_desc=CVE&short_desc_type=allwordssubstr

https://bugzilla.redhat.com/buglist.cgi?bug_status=VERIFIED&bug_status=CLOSED&columnlist=product%2Ccomponent%2Cassigned_to%2Cstatus%2Csummary%2Clast_change_time%2Cseverity%2Cpriority&list_id=13345061&order=priority%2C%20severity%2C%20&query_format=advanced&short_desc=CVE&short_desc_type=allwordssubstr
```
