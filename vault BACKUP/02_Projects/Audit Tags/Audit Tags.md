# Audit Tags
```dataview
TABLE 
  rows.file.link as "Notes",
  length(rows) as "Count"
FROM ""
FLATTEN file.tags as tag
GROUP BY tag
SORT length(rows) DESC
```