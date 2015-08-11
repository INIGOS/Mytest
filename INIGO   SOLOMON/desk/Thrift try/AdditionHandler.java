import org.apache.thrift.TException;

public class AdditionHandler implements AdditionService.Iface {

	@Override
	 public int add(int n1, int n2) throws TException {
	    System.out.println("Add(" + n1 + "," + n2 + ")");
	    return n1 + n2;
	 }

	
}
