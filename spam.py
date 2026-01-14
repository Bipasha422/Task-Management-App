p1="Make a lot of money"
p2="Buy now"
p3="Subscribe this"
p4="click this"
message =input("Enter Your comment:")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):{
print("This comment is a spam")
}
else:{
print("this comment not a spam")}