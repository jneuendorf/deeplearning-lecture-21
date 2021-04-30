"""Use your trained model to predict the digits for the test data. Store the prediction as shown in the code snippet below and upload your prediction file.

Please note that you need to use exactly the shown file format, file name, and array shape as shown in the code snippet. Otherwise, we might not be able to correctly process your submission.
"""

import numpy as np

prediction =  # THAT'S YOUR JOB

# MAKE SURE THAT YOU HAVE THE RIGHT FORMAT
assert prediction.ndim == 1
assert prediction.shape[0] == 2000

# AND SAVE EXACTLY AS SHOWN BELOW
np.save('prediction.npy', prediction)
