---


---

<h1 id="tkinter">Tkinter</h1>
<p>Importation du module Tkinter :</p>
<pre><code>from Tkinter import *
</code></pre>
<p>Création de la fenêtre principale :</p>
<pre><code>fenetre = Tk()
</code></pre>
<p>Boucle d’affichage Tkinter :</p>
<pre><code>fenetre.mainloop()
</code></pre>
<h1 id="widget">Widget</h1>
<pre><code>.pack()
</code></pre>
<p>A ajouter après la déclaration d’un widget pour l’afficher</p>
<h2 id="label">Label</h2>
<p>Affiche du texte ou une image</p>
<pre><code>Label(master=None, options)
</code></pre>
<p>master : widget auquel il est attaché</p>
<p>option notable:<br>
<em>background=<br>
height=<br>
width=<br>
text=<br>
image=</em></p>
<p>Exemple :</p>
<pre><code>from tkinter import *  
fenetre = Tk()  
label = Label(master=fenetre, text="blabla")  
label.pack()  
fenetre.mainloop()
</code></pre>
<p><img src="https://i.imgur.com/BTxd9G9.png" alt="exemple label"></p>
<h2 id="canvas">Canvas</h2>
<p>Affiche une toile sur laquelle on peut dessiner</p>
<pre><code>Canvas(master=None, options)
</code></pre>
<p>Création d’éléments :</p>
<pre><code>  create_rectangle(x1,y1,x2,y2, options)
</code></pre>
<p>Création d’autre forme possible :</p>
<pre><code>create_arc
create_bitmap
create_image
create_line
create_oval
create_polygon
create_rectangle
create_text
create_window
</code></pre>
<p>Exemple :</p>
<pre><code>from tkinter import *  
fenetre = Tk()  
canvas = Canvas(fenetre, width=100, height=100)  
canvas.pack()  
canvas.create_rectangle(40, 33, 60, 77, fill="yellow")  
fenetre.mainloop()
</code></pre>
<p><img src="https://i.imgur.com/dLLwULf.png" alt="exemple canvas"></p>

