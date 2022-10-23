# ---------------------------------------------------------
# from isOdd import isOdd

# print(isOdd(1))
# print(isOdd(4))
# ---------------------------------------------------------

# ---------------------------------------------------------
# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()
# ---------------------------------------------------------

# ---------------------------------------------------------
# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))
# ---------------------------------------------------------

# ---------------------------------------------------------
# import matplotlib.pyplot as plt
# import numpy as np

# Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()


# ls = [1, 2, 3, 2, 7]
# plt.plot(ls)

# plt.show()
# ---------------------------------------------------------


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5739433144:AAHAJrs2WZIYPk2abz6-s6q9lY9eO8otyVk").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()
