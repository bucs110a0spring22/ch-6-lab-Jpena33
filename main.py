import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        #print(n)
        count +=1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    #print(n)                  # the last print is 1
    return(count)

def drawLineGraph(graph=None, x_start=0, y_start=0, x_end=0, y_end=0):
   graph=turtle.Turtle()
   graph.up()
   graph.goto(x_start,y_start)
   graph.down()
   graph.goto(x_end,y_end)

def setUpLineGraph(myscreen=None, graph=None, num_iterations=0, y=0):
  writer=turtle.Turtle()
  max_so_far = 0
  for i in range(1,num_iterations+1):
     result=seq3np1(i)
     if result>max_so_far:
        max_so_far = result
     writer.clear()
     writer.goto(i,result)
     label = str(("Maximum so far: ", i, max_so_far))
     writer.write(label)
     myscreen.setworldcoordinates(0,0,i+10, max_so_far+10)
     
def main():
  userinput = int(input("Please enter upper bound value: "))
  print(userinput)
  if userinput <= 0:
    print("Invalid input")
    exit()
    
  print("Valid input")

  window = turtle.Screen()
  graph = turtle.Turtle()
  window.setworldcoordinates(0,0,10,10)
  drawLineGraph(graph, 0, -10, 0, 20)
  drawLineGraph(graph, -10, 0, 10, 0)
  
  for start in range(1,userinput+1):
    counter = seq3np1(start)
    print("Start is:",start)
    print("Counter is:",counter)
    setUpLineGraph(window, graph, start)
    
  turtle.done()  
    
main()
