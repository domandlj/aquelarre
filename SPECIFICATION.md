# Specification DSL in BNF extended.
# [ ] and * are part of the meta language.

```html
<code> ::= <script-declaration> <code>*
		|  <comment> <code>*
		|  <fun> <code>*

<script-declaration> ::= <script-name> = ./<string>
<script-name> ::= <string>

<comment> ::= #<string>

<cond> ::= <script-name> => <script-name> , <status>	
<fun> ::= <method> <url>: <comment>* <cond>* <comment>* end

<status> ::= <int>

<method> ::= get | post | put | delete | patch

<url> ::= <string> <query>*

<query> ::= ? <param-name> [& <param-name>]*
<param-name> ::= <string>
```
