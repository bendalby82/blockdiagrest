import tempfile
import os
import subprocess
import io

filename = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
print(filename.name)
filename.close()
#Call subprocess
subprocess.call(['blockdiag','test-diags/horizontal-simple-pipeline.txt','-o',filename.name,'-Tpng'])

#Read PNG into a stream
with open(filename.name,'rb') as img:
  pngdata = io.BytesIO(img.read())

pngdata.seek(0)

#Clean up temporary file
os.unlink(filename.name)

#Can now return PNG file to person who called us
mystr = pngdata.read()

print(mystr)
