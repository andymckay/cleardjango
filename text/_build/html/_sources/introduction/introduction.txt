Introduction
--------------------------------------------------------------

Thanks for taking the time to read through this book. Or maybe you are just reading the introduction and then wandering off, let's face it the attention span on the web is small. If that is the case, it was nice meeting you.

Still here, great. First off you are probably asking yourself, another book on Django? There's already a lot of those out there. To prove it, I've made `a list  <http://djangozen.com/books/>`_. Well the reasons are all personal to me, I like Django and I like writing books. That's all there is too it.

I do also think that no matter how well documented a project is and how many books there are, there's always room for more books. That's because people learn in different ways, I've always learned by example. 

Many years ago I had to learn Perl. I've managed to forget most of that now, which is probably good, it allows other things to fit in my brain. There were lots of books I could have read on Perl, but the first one was by Larry Wall himself. As it turns out Larry Wall is not only funny, but a brilliant mind and a great writer. Sadly I found his book impenetrable and got nowhere. 

Then I tried the Perl Cookbook. That just fit my brain beautifully. It showed me how to do things I wanted to know how to do. I don't attack a new language by learning the API, I start with a tutorial then leap from one problem to the next. Finally I'll sit down and figure out all the bits I missed. But for some reason I have to get my first application up and running and so I can proudly display my creation to the world.

Ok maybe that last bit is an exaggeration, it's usually to my dog, Bob. He's a tough critic though.

The Perl Cookbook was a carefully constructed book with recipes that were especially picked so that an audience can follow on from the beginning to the end. If this book is anywhere near as good as that book, I'll be pleased.

Of course Perl needs lots of documentation, Django doesn't. It's second to none in terms of it's documentation. Only a crazy person would write more.

If you are familiar with the cookbooks, then the concept behind this is familiar. If you aren't it's simple. It's full of snippets of code that explain how to complete one idea. These idea's are based on input I've seen on the mailing lists, in chat and experienced. You can read it from front to back and it should make sense, new ideas will be explained, old one's assumed. However you are probably going to want a API book nearby or the Django documentation. This book won't be exhaustive on the API, rather something you will (hopefully) refer back to, time and time again.

Requirements
===============================================================

Before you start, there's one key thing you need. One of them is a working Django installation. That may sound odd, but there's nothing more boring than reading through Chapter 1 on "How to install the frobulator" when all you need to do is a few commands. Since those commands are specific and tailored to your operating system, the best thing to do is go `read the online insallation notes <http://docs.djangoproject.com/en/dev/topics/install/>`_.

Anyway, what does a working Django installation look like? Well the command:::

    python manage.py start
    
should give you something like:::

    Validating models...
    0 errors found

    Django version 1.1 beta 1, using settings 'settings'
    Development server is running at http://127.0.0.1:8000/

    Quit the server with CONTROL-C.

And running:::

    python manage.py shell
    
should give you something like:::

    Python 2.5.2 (r252:60911, Jul 31 2008, 17:31:22) 
    [GCC 4.2.3 (Ubuntu 4.2.3-2ubuntu7)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>>

If any of this doesn't make sense, or gives you errors, then stop. Go read the `installation instructions <http://docs.djangoproject.com/en/dev/topics/install/>`_ again, they are really good. Don't worry I will keep pointing out the superiority of other people's documentation, it's an insecurity thing.

Django is a framework for web developers. So it's assumed that you know:

* How to program using Python.
* How to write HTML.
* How to write bits of JavaScript.
* How the web works, what HTTP is, what a HTTP header is, that the web is stateless and the general inadequacies of the underlying tools and protocols we use to create awesomeness.
* How hard making things pretty across browser is really hard and that if you want a lesson in designing CSS or making things pretty you are in the wrong place.

That first one is the important one. If you don't know how to program in Python, you will be in for a long hard slog. Python is great, go read a good book. It's possible just a day or two off in Python land and you'll feel comfortable enough to come back here. It might take longer, that's fine. Take the time, have a good cup of tea and a long sleep. Maybe a massage. Then come back, it will be easier.

Next bookmark the following in your browser.

* `Python Global Module Index <http://docs.python.org/modindex.html>`_
* `Django documentation <http://docs.djangoproject.com/en/dev/>`_
* `jQuery documentation (if you want to follow the jQuery sections) <http://docs.jquery.com/Main_Page>`_

Next make sure you have access to IRC. Probably the most helpful place in the Django community is the irc channel on the freenode.net IRC server. It's called #django. Any IRC client will set that up, if you are on a Mac I fully recommend `Colloquy <http://colloquy.info/>`_.

There are always people on IRC who are helpful, but it like most places it can take time to learn how to use IRC if you are unfamiliar. Read the topic on the channel once you join and try to ask specific questions rather than general ones. Be prepared to paste errors and tracebacks in to a website, doing it in the channel is rude.

Make sure that you have `Firefox <http://www.mozilla.com/en-US/firefox/firefox.html>`_ handy and that `Firebug <http://getfirebug.com/>`_ extension installed.

Install `Subversion <http://subversion.tigris.org/>`_. Other source code systems are available and I'm sure lots of people will expend lots of energy telling me distributed source code systems will save the planet. My code is in SVN so live with it. If you haven't experienced the joys that SVN can give you and don't want to, then it is available as a zip file too.

Editors
=========================================

I haven't mentioned text editor's or IDE's. That's because I just use `Textmate <http://macromates.com/>`_ and vim. But the latter is mostly just to annoy emacs users. I feel uncomfortable recommending an IDE I don't use and I think it's a very personal thing. I know in other big frameworks starting with J or (curiously) a period, setting up the IDE is one of the first things you do. Open source projects tend not to do that as much. I would recommend my editors, but emacs is cool, so is WingIDE, Komodo and Eclipse. Notepad on the other hand doesn't count. Neither does Microsoft Word.

So rather than talk about how you should work, I'll tell you how I work.

* I use a gorgeous Mac Pro that runs OS X. And I love it all dearly.
* I use Textmate as my editor, as previously noted.
* All my development is done in virtual machines running Ubuntu. When I want to do a new project, I create a new virtual machine off a base image, that has configuration of SVN, ssh keys and the like on it.
* I then use MacFusion to mount the virtual machine using SSHFS.
* Then my text editor is able to edit the Django project as if it was local.
* I can still work in complete isolation on the virtual machine without affecting anything else.

This gives me all the power and advantages of OS X when I need it and Ubuntu where I need it the most. Installing packages that Python or Postgres needs is easy. With this in hand it's easy to create and maintain new projects. How you work is probably different, tell us about it on your blog. If you don't have one yet, a few days with Django will soon solve that.

How the book works
===============================================================

Each recipe has the same structure, the problem, some code, some dissection of the code and then some suggested further readings. It's pretty straightforward. Where possible I've included some form of tests to make sure that the recipe works and always will work.

Please don't go typing too much code in yourself (unless you really want to), all the code is available from SVN. In the next part, we'll discuss how to do this.

Comments and feedback
===============================================================
Are always appreciated, I will try and go through and clean them out occasionally and incorporate them. Particularly tough comments might make go and cry and not write any more recipes for a while. But I will be back. Constructive is good.

License
===============================================================

This is under a Creative Commons Attribution-Noncommercial-Share Alike 3.0 License. Some of the recipes are based on what I've gleaned from blog posts, mailing list posts or other public sources. If that is the case I will attribute the recipe to that person. Any subsequent errors are of course, mine.

If you are the owner of that source and you feel I've done you wrong, please let me know. I'm not sure what I'll do, but it does suck for everyone if someone is unhappy and whilst I can't make the world happy, dammit I can try.