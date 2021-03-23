<div class="hN51TNjcSi3dhlVXQYDNb    "><div class="WYC8upDP4ejko-ykXuJPj "><div class="_2dzsxFsvI3jdb3VJihXKb"><div class="_27CviWae6whkaGxVp7eR3K"><span class="_2kMvStRYHcB_i9hlRV-0v">Difficulty: </span><span class="
  _1WVY8eY9DAX4QCGc7rrgeB
  _1fAs58dBmsp_4PIWi1sQPF" data-tip="Very Hard" currentitem="false"></span></div><div class="_27CviWae6whkaGxVp7eR3K"><span class="_2kMvStRYHcB_i9hlRV-0v">Category: </span><span class="_2_hj2NMN6m6v8war1EsRnx" data-tip="Hidden" currentitem="false">Hidden</span></div><div class="_27CviWae6whkaGxVp7eR3K"><span class="_2kMvStRYHcB_i9hlRV-0v">Successful Submissions: </span><span class="">3,854+</span></div></div><h2 class="_2kWzVNQcgpX8TMmc41Z5bJ">Apartment Hunting<div class="_2LWF317xAqMGBMJQKXTPhx undefined" data-tip="Question Not Submitted" currentitem="false"></div><svg viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg" class="TYL12BIrjlwo6sOv_5iPH"><path d="M12.821 16a.5.5 0 01-.203-.043L8 13.901l-4.618 2.056a.501.501 0 01-.694-.556L3.707 10.3.147 6.732a.502.502 0 01.255-.845l5.103-1.023L7.543.272c.16-.362.753-.362.914 0l2.037 4.592 5.104 1.023a.5.5 0 01.255.845l-3.56 3.567L13.31 15.4a.5.5 0 01-.49.6zM8 12.852c.069 0 .138.015.203.043l3.938 1.754-.882-4.417a.502.502 0 01.137-.452l3.09-3.094-4.441-.89a.5.5 0 01-.36-.288L8 1.708l-1.686 3.8a.5.5 0 01-.36.288l-4.44.89 3.09 3.094c.117.118.169.288.136.452l-.882 4.417 3.939-1.754A.497.497 0 018 12.852z"></path></svg></h2><div class="_2tcVC7w_riRNho_-CSCiNP"><p>
  You're looking to move into a new apartment on specific street, and you're
  given a list of contiguous blocks on that street where each block contains an
  apartment that you could move into.
</p>
<p>
  You also have a list of requirements: a list of buildings that are important
  to you. For instance, you might value having a school and a gym near your
  apartment. The list of blocks that you have contains information at every
  block about all of the buildings that are present and absent at the block in
  question. For instance, for every block, you might know whether a school, a
  pool, an office, and a gym are present.
</p>
<p>
  In order to optimize your life, you want to pick an apartment block such that
  you minimize the farthest distance you'd have to walk from your apartment to
  reach any of your required buildings.
</p>
<p>
  Write a function that takes in a list of contiguous blocks on a specific
  street and a list of your required buildings and that returns the location
  (the index) of the block that's most optimal for you.
</p>
<p>
  If there are multiple most optimal blocks, your function can return the index
  of any one of them.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">blocks</span> = [
  {
    "gym": false,
    "school": true,
    "store": false,
  },
  {
    "gym": true,
    "school": false,
    "store": false,
  },
  {
    "gym": true,
    "school": true,
    "store": false,
  },
  {
    "gym": false,
    "school": true,
    "store": false,
  },
  {
    "gym": false,
    "school": true,
    "store": true,
  },
]
<span class="CodeEditor-promptParameter">reqs</span> = ["gym", "school", "store"]
</pre>
<h3>Sample Output</h3>
<pre>3 <span class="CodeEditor-promptComment">// at index 3, the farthest you'd have to walk to reach a gym, a school, or a store is 1 block; at any other index, you'd have to walk farther</span>
</pre></div><div class="_1Q66kt6DCIqyaVgqslpcDy"><h3 class="_3gIOj5j3LbzNeoKL5U4OnA">Hints</h3><div class="_158jUrYEBViTLqFtt0PXId"><div class="
      _2C2gDZQC2oC7Q_eY_YCsTA
      _1k477lw05gXgZTrVrLVf16
      _3StMMcxlTuTPP68jpGNsII
      
      " tabindex="0"><div class="
      OysSskSl_bF1zRk55Xqlx
      undefined
      _1oa4wmAmh-FSiVjsRHtuhu
      "><div class="_2lfRYaW2XxD3rsz4lT9Crt">Hint 1</div><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 292.362 292.362" class="_2RzU7Ge8gSc-6OW6SFMyDS "><path d="M286.935 69.377c-3.614-3.617-7.898-5.424-12.848-5.424H18.274c-4.952 0-9.233 1.807-12.85 5.424C1.807 72.998 0 77.279 0 82.228c0 4.948 1.807 9.229 5.424 12.847l127.907 127.907c3.621 3.617 7.902 5.428 12.85 5.428s9.233-1.811 12.847-5.428L286.935 95.074c3.613-3.617 5.427-7.898 5.427-12.847 0-4.948-1.814-9.229-5.427-12.85z"></path></svg></div><div class="_2lDvU2UOxnoXbx6AJ9xtAO"><div class="_3amlIFVV5JobPaPbyiOPkZ"><div class="_3i3qSr847X8EMeSirPw1Hs"><p>
For every block, you want to go through every requirement, and for every requirement, you want to find the closest other block with that requirement (or rather, the smallest distance to another block with that requirement). Once you've done that for every requirement and for every block, you want to pick, for every block, the distance of the farthest requirement. You can do this with three nested "for" loops.
</p>
</div></div></div></div></div><div class="_158jUrYEBViTLqFtt0PXId"><div class="
      _2C2gDZQC2oC7Q_eY_YCsTA
      _1k477lw05gXgZTrVrLVf16
      _3StMMcxlTuTPP68jpGNsII
      
      " tabindex="0"><div class="
      OysSskSl_bF1zRk55Xqlx
      undefined
      _1oa4wmAmh-FSiVjsRHtuhu
      "><div class="_2lfRYaW2XxD3rsz4lT9Crt">Hint 2</div><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 292.362 292.362" class="_2RzU7Ge8gSc-6OW6SFMyDS "><path d="M286.935 69.377c-3.614-3.617-7.898-5.424-12.848-5.424H18.274c-4.952 0-9.233 1.807-12.85 5.424C1.807 72.998 0 77.279 0 82.228c0 4.948 1.807 9.229 5.424 12.847l127.907 127.907c3.621 3.617 7.902 5.428 12.85 5.428s9.233-1.811 12.847-5.428L286.935 95.074c3.613-3.617 5.427-7.898 5.427-12.847 0-4.948-1.814-9.229-5.427-12.85z"></path></svg></div><div class="_2lDvU2UOxnoXbx6AJ9xtAO"><div class="_3amlIFVV5JobPaPbyiOPkZ"><div class="_3i3qSr847X8EMeSirPw1Hs">
<p>
Is there a way to optimize on the solution mentioned in Hint #1 (that uses three nested "for" loops) by precomputing the smallest distances of every requirement from every block?
</p>
</div></div></div></div></div><div class="_158jUrYEBViTLqFtt0PXId"><div class="
      _2C2gDZQC2oC7Q_eY_YCsTA
      _1k477lw05gXgZTrVrLVf16
      _3StMMcxlTuTPP68jpGNsII
      
      " tabindex="0"><div class="
      OysSskSl_bF1zRk55Xqlx
      undefined
      _1oa4wmAmh-FSiVjsRHtuhu
      "><div class="_2lfRYaW2XxD3rsz4lT9Crt">Hint 3</div><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 292.362 292.362" class="_2RzU7Ge8gSc-6OW6SFMyDS "><path d="M286.935 69.377c-3.614-3.617-7.898-5.424-12.848-5.424H18.274c-4.952 0-9.233 1.807-12.85 5.424C1.807 72.998 0 77.279 0 82.228c0 4.948 1.807 9.229 5.424 12.847l127.907 127.907c3.621 3.617 7.902 5.428 12.85 5.428s9.233-1.811 12.847-5.428L286.935 95.074c3.613-3.617 5.427-7.898 5.427-12.847 0-4.948-1.814-9.229-5.427-12.85z"></path></svg></div><div class="_2lDvU2UOxnoXbx6AJ9xtAO"><div class="_3amlIFVV5JobPaPbyiOPkZ"><div class="_3i3qSr847X8EMeSirPw1Hs">
<p>
For every requirement, you should be able to precompute its smallest distances from every block by doing two simple passes though the array of blocks: one pass from left to right and one pass from right to left. Once you have these precomputed values, you can iterate through all of the blocks and pick the biggest of all the precomputed distances at that block.
</p></div></div></div></div></div><div class="_158jUrYEBViTLqFtt0PXId"><div class="
      _2C2gDZQC2oC7Q_eY_YCsTA
      _1k477lw05gXgZTrVrLVf16
      _3StMMcxlTuTPP68jpGNsII
      
      " tabindex="0"><div class="
      OysSskSl_bF1zRk55Xqlx
      undefined
      _1oa4wmAmh-FSiVjsRHtuhu
      "><div class="_2lfRYaW2XxD3rsz4lT9Crt">Optimal Space &amp; Time Complexity</div><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 292.362 292.362" class="_2RzU7Ge8gSc-6OW6SFMyDS "><path d="M286.935 69.377c-3.614-3.617-7.898-5.424-12.848-5.424H18.274c-4.952 0-9.233 1.807-12.85 5.424C1.807 72.998 0 77.279 0 82.228c0 4.948 1.807 9.229 5.424 12.847l127.907 127.907c3.621 3.617 7.902 5.428 12.85 5.428s9.233-1.811 12.847-5.428L286.935 95.074c3.613-3.617 5.427-7.898 5.427-12.847 0-4.948-1.814-9.229-5.427-12.85z"></path></svg></div><div class="_2lDvU2UOxnoXbx6AJ9xtAO"><div class="_3amlIFVV5JobPaPbyiOPkZ"><div class="_3i3qSr847X8EMeSirPw1Hs">O(br) time | O(br) space - where b is the number of blocks and r is the number of requirements</div></div></div></div></div></div></div></div>