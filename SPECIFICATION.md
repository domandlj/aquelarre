# Aquelarre formal specification 

## BNF
The specification is in BNF extended, the symbols  
[ ] and * are part of this meta language.

```html
<code> ::= <script-declaration> <code>*
		|  <comment> <code>*
		|  <fun> <code>*

<script-declaration> ::= <script-name> = ./<string>
<script-name> ::= <string>

<comment> ::= #<string>

<cond> ::= not* <script-name> => <script-name> , <status> | <json>, <status>
<fun> ::= <method> <url>: <comment>* <cond>* <comment>* end

<status> ::= <int>

<method> ::= get | post | put | delete | patch

<url> ::= <string> <query>*

<query> ::= ? <param-name> [& <param-name>]*
<param-name> ::= <string>
```
