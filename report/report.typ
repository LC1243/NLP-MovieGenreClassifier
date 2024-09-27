#set page(
  paper: "us-letter",
  numbering: "1",
)

#set par(justify: true)
#set text(
  font: "Linux Libertine",
  size: 11pt,
)

#align(center, text(17pt)[
  *NLP Project*
])

#align(center, text(12pt)[
  Group XX
])

#grid(
  columns: (1fr, 1fr, 1fr),
  align(center)[
    Dr. John Doe \
    Astor Institute \
    #link("mailto:doe@artos.edu")
  ],
  align(center)[
    Dr. John Doe \
    Astor Institute \
    #link("mailto:doe@artos.edu")
  ],
  align(center)[
    Dr. John Doe \
    Astor Institute \
    #link("mailto:doe@artos.edu")
  ]
)


#show: rest => columns(2, rest)

#set heading(numbering: "1.")
#show heading: it => [
  #set text(14pt, weight: "bold")
  #counter(heading).display(it.numbering)
  #smallcaps(it.body) \
]

= Models
#lorem(240)

== Subheading
#lorem(20)

= Experimental Setup
#lorem(250)

= Results
#lorem(100)
//Add table
= Error Analysis
#lorem(110)

= Future Work
#lorem(40)

= References
#lorem(12)
//use bibliography function