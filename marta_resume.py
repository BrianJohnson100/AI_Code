import pprint
import string


def longterm_goals():

    corpus = '''



Experienced and bilingual Customer Service Professional with over 10 years of success in high-volume environments across manufacturing, technology, and engineering sectors. Recognized for delivering exceptional customer support, managing complex sales processes, and serving as the vital link between clients and internal teams. Proven track record of improving service delivery, ensuring customer satisfaction, and maintaining accuracy across ERP and order management systems. Fluent in English and Spanish.

•	Delivered top-tier support to customers by handling order inquiries, status updates, and issue resolution across all phases of the sales cycle.
•	Coordinated closely with engineering and manufacturing teams to ensure timely and accurate order fulfillment.
•	Processed and tracked sales orders using JobBOSS ERP system.
•	Communicated proactively regarding schedule changes, product enhancements, and shipment delays.
•	Managed returns, replacements, and repair inquiries with detailed follow-up.
•	Generated quotes, price information, and supporting product literature to aid sales efforts.
•	Maintained accurate customer documentation and internal reporting to support business transparency.
    '''
    new_corpus = ""

    for letter in corpus.lower():
        if letter in string.ascii_lowercase + " ":
            new_corpus += letter

    corpus_words = new_corpus.split(" ")

    word_count = {}

    for word in corpus_words:

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    pprint.pprint(word_count)

if __name__ == "__main__":
    longterm_goals()