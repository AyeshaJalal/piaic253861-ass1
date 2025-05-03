<H3> PIAIC 253861</H3>

Steps

1.  Import the Decorators
    from a1.message_formatter import decor1, decor2

    This imports two decorators (decor1 and decor2) from a file/module named message_formatter.py in the a1 directory.

    These decorators are:

        decor1: Adds emojis around a message.

        decor2: Adds a border of ✨ above and below a message.

2.  Function Definition with Decorators

        First, decor1(get_name) is called. It wraps get_name() in a new function that:

        Calls get_name()

        Gets its return value (e.g., "Ayesha")

        Adds emojis: 🎉🎀🎉🎀 Ayesha 🎀🎉🎀🎉

        Then, decor2(...) is called on the result of decor1(...).

        It wraps the decorated function from decor1.

        It adds a border above and below the string returned by the inner (emoji-wrapped) function.

        get_name() now does both decorations:

Emoji from decor1

Border from decor2

Decor.py File

Step 1: User Input
Python executes get_name() (now the fully decorated version).

Internally:

It calls decor2's wrapper().

Inside that, it calls decor1's wrapper().

Inside that, it calls the original get_name() function.

That prompts: Enter Your Name:

Suppose user types: Ayesha

Step 2: decor1 Modifies Output
Original get_name() returns "Ayesha"

decor1 wraps it: "🎉🎀🎉🎀 Ayesha 🎀🎉🎀🎉"

Step 3: decor2 Modifies Output
decor2 receives "🎉🎀🎉🎀 Ayesha 🎀🎉🎀🎉" from decor1

It calculates length: len(" 🎉🎀🎉🎀 Ayesha 🎀🎉🎀🎉 ") = 16

Builds border: "✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨"
