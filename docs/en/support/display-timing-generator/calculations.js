(function(root,factory){
  const api=factory()
  if(typeof module==='object'&&module.exports)module.exports=api
  else root.DisplayCalculations=api
})(typeof globalThis!=='undefined'?globalThis:this,function(){
  function mipiBudget(totalRate,ports,lanesPerPort){
    ports=Math.max(1,Number(ports)||1)
    lanesPerPort=Math.max(1,Number(lanesPerPort)||1)
    totalRate=Number(totalRate)||0
    return{totalRate,ports,lanesPerPort,totalLanes:ports*lanesPerPort,perPortRate:totalRate/ports,perLaneRate:totalRate/(ports*lanesPerPort)}
  }
  return{mipiBudget}
})
